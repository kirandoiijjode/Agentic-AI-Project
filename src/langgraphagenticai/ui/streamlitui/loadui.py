import streamlist as st
import os
from datetime import date

from langchain_core import AIMessage, HumanMessage
from src.langraphagenticai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls={}


