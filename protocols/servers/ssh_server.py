'''

This is a ssh server designed to listen for sftp connections
This code came from:

base code came from - https://searchcode.com/codesearch/raw/53300304/

'''


from common import helpers


class Server:

    def __init__(self, cli_object):
        # self.protocol is the protocol that is viewable when using --list-servers
        # This is what the user would use along with --server.  It is the only
        # required attribute of the object.
        # You have complete access to command line arguments
        # within __init__
        # Anything that needs to be set for the server to run should have
        # a self attribute created within __init__
        self.protocol = "ssh"
        self.username = cli_object.username
        self.password = cli_object.password
        self.sftp_directory = helpers.ea_path() + '/data'
        self.port = 22

    # This is the main function that is called by the framework
    # You can build out as many different functions, but they all
    # need to be called from "serve".  If there is a specific function
    # or class that must be seperated out from this file (ideally keep
    # everything in here if possible), then add them to the serverlibs
    # directory
    def serve(self):


        return
