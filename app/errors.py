class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    # def __init__(self, message: str = "Visitor is not vaccinated") -> None:
    #     super().__init__(message)
    def __str__(self) -> str:
        return "Visitor is not vaccinated"


class OutdatedVaccineError(VaccineError):
    def __str__(self) -> str:
        return "All visitors must wear masks"


class NotWearingMaskError(Exception):
    def __str__(self) -> str:
        return "Vaccine is expired"
