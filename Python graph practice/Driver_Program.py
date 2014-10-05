import sys
from SocialNetwork import SocialNetwork

def initialize_graph() -> 'SocialNetwork':
    '''Return a SocialNetwork that is loaded from a file. The name of the file
    to be loaded is provided at the command line or defaults to 'example.timf'
    '''

    # Choose a file name
    graph_filename = (sys.argv[1:] + ['emails.timf'])[0]
    
    # Build and return a graph
    graph = SocialNetwork()
    graph.load_from_file(open(graph_filename))
    return graph
    

def process_input(query: 'list of str', graph: 'SocialNetwork') -> bool:
    '''Handle query commands (friends, degree, etc.) against graph and
    return True iff the 'quit' command is given.
    

    <<friends x>>: list all friends of person x (where x is an e-mail address). 
    Examples:
        >>> friends harold@alias.me
        
        >>> friends hl@imaeatchu.com
        Annie Dr. Evil
        >>> friends andy@toronto.edu
        Brian Law

    <<degree x y>>: print the degree of separation between person x and person y 
    (where people are specified by e-mail address). In the network graph,
    the degree of separation between x and y corresponds to the number of edges 
    on the shortest path between x and y. If there is no path between x and y, 
    then the degree of separation is undefined. Use Python's infinity value 
    float("inf") to represent this value. Notice that a person has 0 degrees of 
    separation with him/herself. 
    Examples:

        >>> degree liudavid@cdf.toronto.edu henry@hyde.net
        2
        >>> degree harold@alias.me andy@toronto.edu
        inf
        >>> degree harold@alias.me harold@alias.me
        0

    <<degrees x d>>: list all people separated from person x by exactly d 
    degrees of separation (where x is an e-mail address). Examples:

        >>> degrees harold@alias.me 100
        
        >>> degrees annie@mgo.org 0
        Annie
        >>> degrees annie@mgo.org 1
        Hannibal Lecter Henry Jekyll
        >>> degrees annie@mgo.org 2
        Anya Tafliovich Dr. Evil

    <<mutual x y>>: list mutual friends of x and y, i.e. 
    people who are friends with both x and y 
    (where people are specified by e-mail address). 
    Examples:
    
    >>> mutual harold@alias.me andy@toronto.edu
        
    >>> mutual dr@evil.net annie@mgo.org
    Hannibal Lecter Henry Jekyll 
    >>> mutual lungj@cdf.toronto.edu sengels@cdf.toronto.edu
    David Liu

    <<likely x>>: suggest missing friends for person x by listing the 
    likeliest missing friends (where x is an e-mail address). 
    The likeliest missing friend is a person who shares the most mutual friends 
    with person x and who is not already a friend of x. Output this list on its 
    own line, separated by spaces. The list should be sorted in alphabetical 
    order. Do not add any other output. For example,

        >>> likely dfinn2003@gmail.com
        
        >>> likely lungj@cdf.toronto.edu
        Anya Tafliovich

    <<classmates x d>>: list all people within d degrees of separation of x 
    who went to the same school (where x is an e-mail address). 

         >>> classmates harold@alias.me 5

         >>> classmates dfinn2003@gmail.com 3
         Rosalie Mullins
         >>> classmates sengels@cdf.toronto.edu 3
         Andy Hwang Brian Law David Liu Dr. Evil Jonathan Lung

    <<quit>>: quit the program
    '''
    
    if len(query) == 2 and query[0] == 'friends':
        print(graph.friends(query[1]))

    elif len(query) == 3 and query[0] == 'degree':
        print(graph.degree_between(query[1], query[2]))

    elif len(query) == 3 and query[0] == 'degrees':
        print(graph.people_with_degree(query[1], query[2]))

    elif len(query) == 3 and query[0] == 'mutual':
        print(graph.mutual_friends(query[1], query[2]))

    elif len(query) == 2 and query[0] == 'likely':
        print(graph.likely_friends(query[1]))

    elif len(query) == 3 and query[0] == 'classmates':
        print(graph.classmates(query[1], query[2]))
                
    elif query == ['quit']:
        return False
        
    else:
        print('Invalid command or wrong number of arguments provided.')
        
    return True

def main():
    '''The main TwitInMyFace program.'''
    
    graph = initialize_graph()

    while process_input(input('>>> ').split(), graph):
        pass            
    
    
if __name__ == '__main__':
    main()