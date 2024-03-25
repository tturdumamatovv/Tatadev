from rest_framework.exceptions import APIException

class DuplicateReviewError(APIException):
    status_code = 400
    default_detail = 'You have already submitted a review for this restaurant.'
    default_code = 'duplicate_review'
