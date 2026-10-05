from pydantic import BaseModel


class PredictionRequest(BaseModel):
    """One trial's first-3-day base aggregates, as the caller knows them."""

    # TODO: declare the seven fields a caller must send, one line each,
    # with a type for each. They are the same seven base aggregates your
    # feature code starts from; features.py names them.

    sessions_day1: int
    sessions_day2: int
    sessions_day3: int
    listen_sessions_3d: int
    total_minutes_3d: int
    country: str
    device_type: str




class PredictionResponse(BaseModel):
    """What we send back: a probability and a band a human can act on."""

    conversion_probability: float
    conversion_band: str
