#!/usr/bin/env python
#-*- coding: utf-8 -*-




#
# DESCRIPTION
#
# a test application to check for functionalities realized within the freeplane
# library
#
#
# AUTHOR
#
#   - Nnamdi Kohn, 2022
#




# general
import argparse
import os
import re
import sys
import logging
import inspect

# application specific
import freeplane
#import freeplane_model as model

# dev
from encryption_MD5WithDES import PBEWithMD5AndDES
from encryption_MD5WithDES import PBEWithMD5AndTripleDES




#
# main routine
#

if __name__ == "__main__":




    #
    # settings
    #

    # these settings might be replaced with arguments read from CLI or API

    # strProjectPath          = 'c:\\Users\\pkohn\\_NEXTCLOUD\\_TOOLS\\_Python\\LIB__freeplane'
    # strModule               = 'freeplane'
    # strModuleFilename       = strModule + '.py'
    # strMindmapPath          = strProjectPath + '\\freeplane.mm'
    # strModulePath           = strProjectPath + '\\src\\' + strModuleFilename
    # strExample1NodeId       = "ID_639295227"
    # strResult1ParentNodeId  = "ID_1935110449"




    #
    # load existing mindmap
    #

    # mindmap = freeplane.Mindmap(strMindmapPath, log_level="debug")




    #
    # read node contents
    #

    # _node = mindmap.find_nodes(id=strExample1NodeId)[0]
    # _text = _node.model.text_as_list_of_lines




    #
    # print content
    #

    # print(_text)




    #
    # encrypt some content
    #

    # create security object
    # password        = "taboo"
    # password        = "test"
    # plain_text      = "dies ist ein kleiner Test!"
    # encrypted_text  = cipher.encrypt(plain_text, password)
    # encrypted_text  = b"fUg00upinp0=m9wdrklgLvVa3SKgget9xzW+6OPALUJ4bK18FeBcGUG9rg1qC0wqKbjJdUhjHqXwYnn6xcJBN5++Z0AL3i6sPvEjvg5L1cF6qZKv2sX/p1Q33xA6lb1G3gvGREg7fVSzwrLs8T0yiMUqFv0/K9Vj0fgoa4ArKYmVa4nd9Jh34ntNiAlDj8GUmOnLwQRs/8I00ax/DByMAjhJ5dGVYKR4i6Ni3zabaqyarKvjKbO0vDQj1kGEczJ9O2Jj/tl2xM3D0J8bCfaRJUyaTcgn+uI81RRXpFz+pmVo0gZ813KdCWeeJLd8fqrHPZeWUjrcAgG/Ul8UapwQ7KPzFUQQrDefTR0hWJr9YGahqYibTllDveT63iezdHxQWoLUmbmktLtY00gSKqQli1kQSsRXM0cw4Kcn5KnfqKUXfAcJUc61PgidnGAAqA1o9FR/kO5Y0JKR"




    #
    # decrypt some content
    #

    password        = "test"

    encrypted_text = "waYBJ8/rGlc= fomZt+sBoGI+YKuZmiiumUqOF8Y/C+yfMdW75p7vmbCkiAU5uR3in5V2VmV7IYZGeeFFSmbPansR+5C5LKh0Yf8QZJjO6RZDHHA56AvuMHEtApXOUPiaJfQbiZpHOTvO0YXObA5FVWIxDlyhIDXZabmKDKpaTFFtM572PW+UQg/I051PVwY2/Zy8bwtrENFgZhKPn5l55UbI7eBcJ235r07Gmw2Xe0c7zgudjzVolhfy147m4MuAxM2Fbl1c75D1huCaWv4Oa9RLfKtntXcnJtRH1a1cyOxIovgYw05F6LY0E9F1BIfq6B6dmOURhXZssd6SaG1csC7ko+T67Zt8ZCakGK6U+suEn6RYw1RllKb1b6ORx11nVxT2gA5+05VwNLm1JhwBpYeseyA0vX257oF5agVs5qaG+lRDUSz+H91Xl9Ht1BVF/5AbSeh40DTkB6Qy4kvHfEQmbl7iE66hzzL4QD9TXYsgWtPkaEbT4SPKf7bTmWMabScGvzCXhUVHI4ayf8960dTfBfd/ooARkpbvhjI9BDIsTRlXekGnX64s3j3V1YJLBq6pYw25tgb3zUkFuR0lK4INIlwwDcIw88PAX84+TqBG3WqM/FepEaGFW67vOag2p+8Mq+Kk+EOPXHBUlKgnn5rj66SER+mUMg65U+Vd2c7SsDr6OI2NWxSX4ErRMgHXK5as19O+9AOVFU4VF9ObPLmZVkU1Zr7HvOLduoqIHM2Sdr6XOpEXLFbIIhtEl6cwC3qawz5zos4QylKKNUxyPsECnf1ApMSPXSH7Kmg2YdRirgd40h1k3J6Am28aiFWxbWCwEtOkz3/3i3RZBpaD5mwQT3sreGxXVQ=="

    # cipher          = PBEWithMD5AndDES()
    cipher          = PBEWithMD5AndTripleDES()
    decrypted_text  = cipher.decrypt(encrypted_text, password)

    print(decrypted_text)




    #
    # save mindmap
    #

    #mindmap.save(strMindmapPath)
