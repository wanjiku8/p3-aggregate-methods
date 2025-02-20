class Student:
    def __init__(self, name):
        self.name = name
        self._enrollments = []
        self._grades = {}

    def enroll(self, enrollment, grade):
        """Adds an enrollment and assigns a grade."""
        self._enrollments.append(enrollment)
        self._grades[enrollment] = grade

    def course_count(self):
        """Returns the number of courses the student is enrolled in."""
        return len(self._enrollments)

    def aggregate_average_grade(self):
        """Returns the average grade across all courses for the student."""
        if not self._grades:
            return 0  
        return sum(self._grades.values()) / len(self._grades)
