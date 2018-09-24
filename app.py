import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
from db.db import Database
from spotify.spotify import Spotify
import time
import asyncio
from timeit import default_timer as timer

DBHandler = Database()
SpotifyHandler = Spotify()

MAX_ID = 10



# def run_search():

  # starting_user_id = int(DBHandler.find_max_user_id())
  # starting_user_id += 1

  # MAX_ID = 1000000000

  # for i in range(starting_user_id, MAX_ID):
  #   id_string = str(i).zfill(10)
  #   print('retrieving playlists for user: ' + id_string)
  #   playlists = SpotifyHandler.get_full_playlists_for_user(id_string)
  #   if len(playlists) > 0:
  #     for i, playlist in enumerate(playlists):
  #       display_same_line("storing... " + str(i+1) + " of " + str(len(playlists)) + " for spotifyUID: " + id_string)
  #       DBHandler.upsert_playlist({ 'id': playlist['id'] }, playlist)

  #   print("marking user " + id_string + " completed")
  #   DBHandler.upsert_user({ 'id': id_string }, { 'id': id_string, 'hasBeenSearched': True })


def display_same_line(message):
  print(message.ljust(50), end="\r")


async def search_user_async(user_id):
  playlists = SpotifyHandler.get_full_playlists_for_user(user_id)
  if len(playlists) > 0:
    for i, playlist in enumerate(playlists):
      print("storing... " + str(i+1) + " of " + str(len(playlists)) + " for spotifyUID: " + user_id)
      DBHandler.upsert_playlist({ 'id': playlist['id'] }, playlist)
  return { "completed": True, "user_id": user_id }

async def search_users_async(user_ids):
  start = timer()
  parallel_calls = [search_user_async(user_id) for user_id in user_ids]
  completed, pending = await asyncio.wait(parallel_calls)
  end = timer()
  print("fucking done! " + str(end-start) + " elapsed")
  for item in completed:
    print(item)

# @app.route('/')
# def todo():
#   return render_template('todo.html', items=items)


# @app.route('/new', methods=['POST'])
# def new():
#     return redirect(url_for('todo'))


event_loop = asyncio.get_event_loop()
try:
  event_loop.run_until_complete(search_users_async([
                                              '000000001',
                                              '000000002',
                                              '000000003',
                                              '000000004',
                                              '000000011',
                                              '000000006',
                                              '000000007',
                                              '000000008',
                                              '000000009',
                                              '000000010',
                                              '000000001',
                                              '000000002',
                                              '000000003',
                                              '000000004',
                                              '000000011',
                                              '000000006',
                                              '000000007',
                                              '000000008',
                                              '000000009',
                                              '000000010',
                                              '000000001',
                                              '000000002',
                                              '000000003',
                                              '000000004',
                                              '000000011',
                                              '000000006',
                                              '000000007',
                                              '000000008',
                                              '000000009',
                                              '000000010',
                                              '000000001',
                                              '000000002',
                                              '000000003',
                                              '000000004',
                                              '000000011',
                                              '000000006',
                                              '000000007',
                                              '000000008',
                                              '000000009',
                                              '000000010',
                                              '000000001',
                                              '000000002',
                                              '000000003',
                                              '000000004',
                                              '000000011',
                                              '000000006',
                                              '000000007',
                                              '000000008',
                                              '000000009',
                                              '000000010',
                                              '000000001',
                                              '000000002',
                                              '000000003',
                                              '000000004',
                                              '000000011',
                                              '000000006',
                                              '000000007',
                                              '000000008',
                                              '000000009',
                                              '000000010',
    ]))
finally:
  print('closing loop')
  event_loop.close()



# retries = 0
# while retries < 1000:
#   try:
#     run_search()
#   except:
#     retries += 1
#     print("exception experienced. sleeping for 5 secs... " + str(1000-retries) + " retries remaining")
#     time.sleep(5)


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=PORT, debug=True)