class Customer:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return self._first_name
    
    def set_first_name(self, first_name):
        if type(first_name) == str and 1 <= len(first_name) <= 25:
            self._first_name = first_name
        else:
            raise Exception
        
    def get_last_name(self):
        return self._last_name
    
    def set_last_name(self, last_name):
        if type(last_name) == str and 1 <= len(last_name) <= 25:
            self._last_name = last_name
        else:
            raise Exception
        
    first_name = property(get_first_name, set_first_name)
    last_name = property(get_last_name, set_last_name)

    def reviews(self):
        from classes.review import Review
        return [review for review in Review.all if review.customer == self]
    
    def restaurants(self):
        from classes.review import Review
        return [review.restaurant for review in Review.all if review.customer == self]

    def num_reviews(self):
        from classes.review import Review
        count = 0

        for review in Review.all:
            if review.customer == self:
                count += 1

        return count
