class CartListMovieObject:
    def __init__(self, movie_id, quantity):
        self.movie_id = movie_id
        self.quantity = quantity


class CartObject:
    def __init__(self, items, total, total_qty):
        self.items = items