import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml
from

class SQLQueryToLinkedList():

    def __init__(self, base_github_folder):
        self.base_github_folder = base_github_folder

    def stringToListNode(stringTotal):
        previousNode = None
        first = None
        for i in stringTotal:
            currentNode = ListNode(i)
            if first is None:
                first = currentNode
            if previousNode is not None:
                previousNode.next = currentNode
            previousNode = currentNode
        return first

if __name__ == "__main__":


