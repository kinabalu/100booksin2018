from apistar import Include, Route
from project.views import getReadList, getToReadList

routes = [
    Route('/getread', 'GET', getReadList),
    Route('/gettoread', 'GET', getToReadList)
]
