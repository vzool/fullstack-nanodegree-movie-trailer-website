import webbrowser, os, re, sys, time, BaseHTTPServer, threading
from SimpleHTTPServer import SimpleHTTPRequestHandler
from app.view import main_page_head, main_page_content, movie_tile_content

# Thread function to open website after deploy automatically
def open_website_after_deploy(url):
    """Thread function to open website after deploy automatically"""
    # sleep 1 second
    time.sleep(1)
    # open website
    webbrowser.open(url, new=2)
    return
    
# Webserver function
def start_webserver():
  """WebServer"""
  # change location of current working directory to app/http
  # So, The browser will found index.html
  os.chdir('app/http')

  # check if there is a parameter
  if sys.argv[1:]:
    try:
      port = int(sys.argv[1]) # CLI Parameter port if exists
    except:
      print("Error: check your parameter.")
      quit()

  else:
    port = 13579 # Default port

  # create a tuble with (ip, port)
  server_address = ('127.0.0.1', port)

  # assign the protocol
  SimpleHTTPRequestHandler.protocol_version = "HTTP/1.0"
  httpd = BaseHTTPServer.HTTPServer(server_address, SimpleHTTPRequestHandler)

  # get socket name
  sa = httpd.socket.getsockname()

  # notify user
  print "Serving 'Movie Trailer Website' on", sa[0], "port", sa[1], "..."

  # parse url from socket instance
  url = "http://" + str(sa[0]) + ":" + str(sa[1])
  # create a Thread instance
  thread = threading.Thread(target=open_website_after_deploy, args=(url,))
  # start thread
  thread.start();

  # http server loop
  httpd.serve_forever()

def create_movie_tiles_content(movies):

    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.html.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def open_movies_page(movies):

  # Create or overwrite the output file
  output_file = open('app/http/index.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.html.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head.html + rendered_content)
  output_file.close()

  # start WebServer
  start_webserver()
