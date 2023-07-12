from classes.customer import Customer
from classes.restaurant import Restaurant

class Review:
    all = []
    
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.add_review(self)

    @classmethod
    def add_review(cls, review):
        cls.all.append(review)

    def get_customer(self):
        return self._customer
    
    def set_customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception
        
    def get_restaurant(self):
        return self._restaurant
    
    def set_restaurant(self, restaurant):
        if isinstance(restaurant, Restaurant):
            self._restaurant = restaurant
        else:
            raise Exception

    def get_rating(self):
        return self._rating
    
    def set_rating(self, rating):
        if type(rating) == int and 1 <= rating <= 5:
            self._rating = rating
        else:
            raise Exception

    customer = property(get_customer, set_customer)
    restaurant = property(get_restaurant, set_restaurant)
    rating = property(get_rating, set_rating)