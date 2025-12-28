import structlog
from collections import OrderedDict


def move_event_to_front(_, __, event_dict):
    if "event" in event_dict:
        event = event_dict.pop("event")
        return OrderedDict([("event", event), *event_dict.items()])
    return event_dict


structlog.configure(
    processors=[
        move_event_to_front,   # type: ignore
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ]
)


def get_logger(name: str = None) -> structlog.BoundLogger:
    return structlog.get_logger(name=name)
