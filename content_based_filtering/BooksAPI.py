import requests, json, os, time
from urllib.parse import urlencode

dir_path = os.path.dirname( os.path.realpath(__file__))
gg_apikey = 'AIzaSyD6L7oqtx2VvGWfMHwfdIw7NmZm1O13Utw'

def GoogleBookAPI():
    url = 'https://www.googleapis.com/books/v1/volumes'
    headers = { 'Accept': 'application/json'}
    params = {
        'key': gg_apikey,
        'q': 'isbn:0002005018,0195153448'
    }
    data = requests.post(url , headers = headers, data = params)

    if data.status_code == 200:
        print( data.text)
    else:
        print(f'Request failed with status code: {data.status_code}')

def encode_isbn( isbn_list):
    str_isbn = ''
    for isbn in isbn_list:
        str_isbn += 'ISBN:' + isbn + ','
    return str_isbn[:-1]

def OpenLibAPI( isbn_list , verbose = False):
    url = 'http://openlibrary.org/api/books?'
    str_isbn = encode_isbn(isbn_list)
    params = {
        'bibkeys': str_isbn,
        'format': 'json',
        'jscmd' : 'details'     #'details' or 'data'
    }
    r_url = url + urlencode(params)
    if verbose:
        print( f'Getting data for {r_url}')

    data = requests.get( r_url )

    if data.status_code == 200:
        d_json = json.loads( data.text )

        if verbose:
            print(f'Received json file of the length: {len(d_json)}')

        return d_json
    else:
        if verbose:
            print(f'Request failed with status code: {data.status_code}')

        return None

def GetISBN( path = 'isbn_toscrape.csv'):
    with open( path ) as fh:
        isbn_list = fh.read().splitlines()
    return isbn_list

def chunks(l, n):
    """
    Yield successive n-sized chunks from l.
    source: https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
    """
    for i in range(0, len(l), n):
        yield l[i:i + n]

def Main():
    isbn_list = GetISBN(dir_path + '/isbn_toscrape.csv')
    print(f'We have {len(isbn_list)} ISBNs')

    batch_size = 10
    isbns_batches = chunks( isbn_list, batch_size)

    for i, batch in enumerate(isbns_batches):
        print(f'--- Working on {i+1} of {int(len(isbn_list) / batch_size)} batches of ISBNs')

        s_time = time.time()
        json_data = OpenLibAPI( batch )
        e_time = time.time()
        print(f'Downloaded data for {len(json_data)} in {"{:.2f}".format((e_time - s_time)/60)} minutes.')

        output_path = dir_path + '/book_data/openlib_book_data_' + str(i+1) + '.json'
        print(f'Outputting Book Data File to {output_path}')
        with open(output_path, 'w') as fh:
            json.dump( json_data, fh)

Main()
