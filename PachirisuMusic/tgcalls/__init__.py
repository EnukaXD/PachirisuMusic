from os import listdir, mkdir
from pyrogram import Client
from PachirisuMusic import config
from PachirisuMusic.tgcalls.queues import clear, get, is_empty, put, task_done
from PachirisuMusic.tgcalls import queues
from PachirisuMusic.tgcalls.youtube import download
from PachirisuMusic.tgcalls.calls import run, pytgcalls
from PachirisuMusic.tgcalls.calls import client

if "raw_files" not in listdir():
    mkdir("raw_files")

from PachirisuMusic.tgcalls.convert import convert
