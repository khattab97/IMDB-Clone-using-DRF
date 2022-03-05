from rest_framework.throttling import UserRateThrottle


class ReviewListThrottling(UserRateThrottle):
    scope = 'review-list'


class ReviewCreateThrottling(UserRateThrottle):
    scope = 'review-create'
