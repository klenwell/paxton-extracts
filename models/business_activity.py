class BusinessActivity:
    def __init__(self, **params):
        self.resource = params.get('resource')
        self.owner = params.get('owner')
        self.started_at = params.get('started_at')
        self.ended_at = params.get('ended_at')
        self.created_at = params.get('created_at')
        self.title = params.get('title')
        self.description = params.get('description')
        self.url = params.get('url')
        self.api_data = params.get('data')

    #
    # Static Methods
    #
    @staticmethod
    def from_email_message(message):
        activity = BusinessActivity(
            resource='email',
            owner=message.sender.address,
            started_at=message.sent,
            ended_at=message.received,
            created_at=message.created,
            title=message.subject,
            description=message.body_preview,
            url=message.web_link
        )

        activity.set_api_data_safely(message)
        return activity

    @staticmethod
    def from_calendar_event(event):
        activity = BusinessActivity(
            resource='meeting',
            owner=event.organizer.address,
            started_at=event.start,
            ended_at=event.end,
            created_at=event.created,
            title=event.subject,
            description=event.get_body_text(),
            url=None
        )

        activity.set_api_data_safely(event)
        return activity

    #
    # Properties
    #
    @property
    def date(self):
        return self.started_at.date()

    @property
    def start_time(self):
        return self.started_at.time()

    @property
    def duration(self):
        if self.resource == 'meeting':
            return (self.ended_at - self.started_at)
        else:
            return None

    #
    # Instance Methods
    #
    def to_csv(self):
        return [
            self.date,
            self.resource,
            self.started_at,
            self.ended_at,
            self.start_time,
            self.duration,
            self.title,
            self.owner,
            self.description
        ]

    def set_api_data_safely(self, o365_record):
        """In Python 3.8.0, this was causing an error. It was not a problem with
        later versions, but platform on which I currently relay is still
        on 3.8.0.
        """
        try:
            self.api_data = o365_record.to_api_data()
        except TypeError as e:
            f = "Caught error on O365 object to_api_data method:\n  {}\n  {}"
            print(f.format(e, o365_record))

    def __repr__(self):
        f_ = '<BusinessActivity ({}) title="{}" date={}>'
        return f_.format(self.resource, self.title, self.date)
