from dataclasses import dataclass
 

@dataclass(frozen=True)
class BMICategory:
	"""
	Represents a specific BMI classification range.
	
	Attributes:j
		name (str): The label of the category (e.g., 'Normal Weight').
		min_bound (float): The lower boundary of the BMI range (inclusive).
		max_bound (float | None): The upper boundary of the BMI range (exclusive) or None for open-end category.
	"""
	name: str
	min_bound: float
	max_bound: float | None
	
	
	def __post_init__(self):
		if self.min_bound < 0:
			raise ValueError(f"min_bound must be non-negative, got {self.min_bound}")
		
    if self.max_bound is not None and self.max_bound <= self.min_bound:
			raise ValueError(f"max_bound ({self.max_bound}) must be greater than min_bound ({self.min_bound})")
	
	
	def contains(self, bmi_value: float) -> bool:
		"""
		Encapsulates the range evaluation logic.
		
		Args:
			bmi_value (float): The calculated BMI score to check.
			
		Returns:
			bool: True if the value falls within the bounds, False otherwise.
		"""
		if self.max_bound is None:
			return self.min_bound <= bmi_value
		
		return self.min_bound <= bmi_value < self.max_bound


# Predefined BMI Categories
CATEGORIES: tuple[BMICategory, ...]= (
	BMICategory("Underweight", 0, 18.5),
	BMICategory("Normal", 18.5, 25),
	BMICategory("Overweight", 25, 30),
	BMICategory("Obese", 30, None),
)

