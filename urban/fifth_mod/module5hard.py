#!/usr/bin/env python


import hashlib
import time
import re
import sys


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.__set_password(password)
        self.age = age

    def __hash_password(self, password):
        return hashlib.sha3_256(password.encode()).hexdigest()

    def __is_valid_password(self, password):
        pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[\W_]).{12,}$'
        return re.match(pattern, password) is not None

    def __set_password(self, password):
        if self.__is_valid_password(password):
            return self.__hash_password(password)
        else:
            print('The password does not meet the security criteria.')
            sys.exit(1)

    def __str__(self):
        return self.nickname

    def __repr__(self):
        return f'User(nickname={self.nickname}, age={self.age})'

    def __eq__(self, other):
        return isinstance(other, User) and self.nickname == other.nickname and self.password == other.password


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Video(title={self.title}, duration={self.duration}, time_now={self.time_now}, adult_mode={self.adult_mode})'

    def __eq__(self, other):
        return isinstance(other, Video) and self.title == other.title


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                return
        print('Invalid login or password')

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f'User {nickname} already exists')
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(existing_video.title == video.title for existing_video in self.videos):
                self.videos.append(video)

    def get_videos(self, search_term):
        search_term = search_term.lower()
        return [video.title for video in self.videos if search_term in video.title.lower()]

    def watch_video(self, title):
        if self.current_user is None:
            print('Login to watch video')
            return

        video = next((v for v in self.videos if v.title == title), None)
        if video is None:
            print('Video not found')
            return

        if video.adult_mode and self.current_user.age < 18:
            print('You are under 18 years old, please leave the page')
            return

        for second in range(video.duration):
            print(second + 1, end=' ')
            time.sleep(1)
        print('End of video')
