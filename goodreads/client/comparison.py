

class Comparison:
    """
    Data Members:
        not_in_common
        your_library_percent
        their_library_percent
        your_total_books_count
        their_total_books_count
        common_count
        reviews (list of dictionaries)
            book
                title
                id
            your_rating
            their_rating
    """
    def __init__(self, compare_dict):
        """ Parse dictionary for useful data """
        for key, val in compare_dict.items():
            if key == 'reviews':
                reviews = []
                for review_dict in val['review']:
                    review = {}
                    review['title'] = review_dict["book"]['title']
                    review['id'] = review_dict["book"]['id']
                    review['your_rating'] = review_dict["your_review"]['rating']
                    review['their_rating'] = review_dict["their_review"]['rating']
                    reviews.append(review)
                self.__dict__[key] = reviews
                continue
            self.__dict__[key] = val

