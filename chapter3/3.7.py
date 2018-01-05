import sys
sys.path.insert(1, "C:\Users\Tim\Desktop\competition\clrs\datastructures_old_py2")
from datastructures.queue import Queue
from datastructures.linkedlist import LinkedList, Node


class AnimalQueue(object):
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
        self.order = 0

    def enqueue(self, animal):
        animal.order = self.order
        self.order += 1
        if isinstance(animal, Dog):
            self.dogs.enqueue(animal)
        if isinstance(animal, Cat):
            self.cats.enqueue(animal)

    def dequeue_any(self):
        if self.dogs.queue_empty():
            return self.dequeue_cat()
        elif self.cats.queue_empty():
            return self.dequeue_dog()
        elif self.dogs.peek().order < self.cats.peek().order:
            return self.dequeue_dog()
        else:
            return self.dequeue_cat()

    def dequeue_dog(self):
        return self.dogs.dequeue()

    def dequeue_cat(self):
        return self.cats.dequeue()


class Animal(object):
    def __init__(self):
        self.order = None


class Dog(Animal):
    pass


class Cat(Animal):
    pass


# class AnimalQueue2(object):
#     def __init__(self):
#         self.dogs = LinkedList()
#         self.cats = LinkedList()
#         self.both = LinkedList()

#     def enqueue(self, animal):
#         if isinstance(animal, Dog):
#             self.dogs.insert_tail(animal.animal_node)
#         elif isinstance(animal, Cat):
#             self.cats.insert_tail(animal.animal_node)
#         self.both.insert_tail(animal.both_node)

#     def dequeue_any(self):
#         animal = self.both.head
#         if animal is not None:
#             self.both.delete(animal)
#             self.dogs.delete(animal.key.animal_node)
#             self.cats.delete(animal.key.animal_node)
#         return animal

#     def dequeue_dog(self):
#         dog = self.dogs.head
#         if dog is not None:
#             self.dogs.delete(dog)
#             self.both.delete(dog.key.both_node)
#         return dog

#     def dequeue_cat(self):
#         cat = self.cats.head
#         if cat is not None:
#             self.cats.delete(cat)
#             self.both.delete(cat.key.both_node)
#         return cat


# class Animal2(object):
#     def __init__(self):
#         self.animal_node = Node(self)
#         self.both_node = Node(self)


# class Dog(Animal2):
#     pass


# class Cat(Animal2):
#     pass


aq = AnimalQueue()
for _ in xrange(10):
    aq.enqueue(Dog())
    aq.enqueue(Cat())
print aq.dogs
print aq.cats
for _ in xrange(10):
    print type(aq.dequeue_dog())
print aq.dogs
print aq.cats
