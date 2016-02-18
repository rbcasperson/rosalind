import os.path

def grab_input(rosalind_problem_name, downloads_directory):
    """
    Opens a text file representing rosalind input to solve a problem.
    Pass in the name of the current rosalind problem name to look it up
    in your downloads directory, where rosalind text files typically end up.

    >>> grab_input('rosalind_ini3.txt')
    wpoR2sT77ULTxwXaC9DNJKsM2jSUFlaDvhySPNATyhO92brubeDVnRXnx6YYzS88UHolodact
    ylusbDN4pAeMJiGTF0IWa0u8VSWrBcJXmog5JI0kDVyklRxUxkCZihLQ1aJwqFhemilasiusw
    hlfQ1AxRYA6H3QNFTcNnNiWfn7cuE.
    65 76 135 144
    """
    if downloads_directory is None:
        downloads_directory = '~/Downloads'
    downloads_directory = os.path.expanduser(downloads_directory)
    return open(os.path.join(downloads_directory, rosalind_problem_name), 'r').read()

if __name__ == '__main__':
    # you've called this from the command line
    import argparse
    import importlib

    parser = argparse.ArgumentParser(
        description=(
            '''
            Solve a rosalind problem. Make sure you name your python file that contains
            the `main` function the same thing as the text file you downloaded from rosalind.
            '''
        )
    )

    parser.add_argument(
        'problem_name',
        action='store',
        help='the name of the file you downloaded for this problem, minus the extension'
    )

    parser.add_argument(
        '--downloads-directory',
        action='store',
        help='the directory where your rosalind downloads end up'
    )

    args = parser.parse_args()
    rosalind_solver = importlib.import_module(args.problem_name)
    rosalind_input = grab_input(args.problem_name + '.txt', args.downloads_directory)

    print rosalind_solver.main(rosalind_input)