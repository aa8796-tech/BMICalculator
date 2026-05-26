from dataclasses import dataclass
from collections.abc import Iterable

@dataclass(frozen=True)
class BMICategory:
	"""
	Represents a specific BMI classification range.
	
	Attributes:
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
		
		
def calculate_bmi(weight: float, height: float) -> float:
	"""
	Calculates the Body Mass Index (BMI) using weight and height.
	
	Args:
		weight (float): Weight in kilograms.
		height (float): Height in meters.
		
	Returns:
		float: The calculated BMI value.
		
	Raises:
		ValueError: If weight or height is less than or equal to zero.
	"""
	if height <= 0 or weight <= 0:
		raise ValueError("Weight and height must be positive values greater than zero.")
	return weight / (height ** 2)


def get_category(bmi: float, categories: Iterable[BMICategory]) -> BMICategory:
	"""
	Evaluates and matches a BMI score against a collection of dynamic categories.
	
	Args:
		bmi (float): The BMI score to classify.
		categories (Iterable[BMICategory]): An iterable collection of configured BMI ranges.
		
	Returns:
		BMICategory: The matching category object.
		
	Raises:
		ValueError: If the BMI value does not map to any provided category.
	"""
	for category in categories:
		if category.contains(bmi):
			return category
			
	raise ValueError(f"Uncategorized BMI value: {bmi}")
