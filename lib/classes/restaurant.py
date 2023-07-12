
class Restaurant:

    '''
        Was strugging to make the Restaurant.name unchangeable, I tried to
        make the set_name() as:
        
        set_name(self, name):
            raise Exception

        but this would just make all of my other unit tests raise an exception.
        I was able to pass all of the other tests however. 
    '''

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and len(name) >= 1 and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception

    name = property(get_name, set_name)

    def reviews(self, new_review=None):
        from classes.review import Review
        return [review for review in Review.all if review.restaurant == self]
    
    def customers(self, new_customer=None):
        from classes.review import Review
        return [review.customer for review in Review.all if review.restaurant == self]

    def average_star_rating(self):
        from classes.review import Review
        rating_count = 0
        rating_total = 0

        for review in Review.all:
            if review.restaurant == self:
                rating_count += 1
                rating_total += review.rating

        return rating_total/rating_count

    @classmethod
    def get_all_restaurants(cls):
        pass

