# todo: Решить надо это или нет. Это обертка для класса, чтоб сделать его мультитоном, но необходимость отпала,
#  т.к. поставил уникальное имя. Повторяющийся хаб завести нельзя.

# def multiton(cls):
#     instances = {}
#
#     def getinstance(id):
#         if id not in instances:
#             instances[id] = cls(id)
#         return instances[id]
#
#     return getinstance
