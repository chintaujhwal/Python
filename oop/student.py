class student:
    # constructor
    def __init__(self, name, course):
        # object attributes
        self.name = name
        self.course = course
        self.fee_paid = 0

    @property
    def course_fee(self):
        if self.course == "Python":
            return 4000
        if self.course == "C":
            return 1000
        if self.course == "Java":
            return 2500

    def pay(self, amount):
        if self.fee_paid + amount > self.course_fee:
            raise ValueError("Excess amount paid...!")
        else:
            self.fee_paid += amount

    @property
    def due(self):
        return self.course_fee - self.fee_paid


s1 = student("Eleven", "C")

print(s1.course_fee)
s1.pay(800)
print(s1.due)