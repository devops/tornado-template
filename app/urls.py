#!/usr/bin/env python2
# -*- coding: UTF-8 -*-

import api.v1.index
import index

urls = api.v1.index.urls \
        + index.urls
