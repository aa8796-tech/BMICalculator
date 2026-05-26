from collections.abc import Iterable
from categories import BMICategory

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
