# sanic-app Created by zhengzongwei on 2021/04/07
# Copyright (c) 2021 zhengzongwei. All rights reserved.

from app import create_app
app = create_app('develop')


if __name__ == '__main__':
    app.run()