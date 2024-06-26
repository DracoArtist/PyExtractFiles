text = """
    This script will walk through a directory of your choice and copy
        all PDF (and/or other types of) files into a second directory.

    To use this script, you will need 3 things:
    1. The path to the directory from which you want to copy your files
        (this is `source_directory`).
    2. The path to the directory where you want to store your copies
        (this is `target_directory`). You need to create this folder before running
        the code; it will not be created automatically.
    3. The extension of the files you want to copy. The default is .pdf

    **WARNING:** To avoid errors during execution, ensure that `target_directory`
        is NOT within `source_directory`.

    Example of a good directory structure:
    - root_directory
        - source_directory
            - some files
        - target_directory

    Example of a problematic directory structure:
    - root_directory
        - source_directory
            - some files
            - target_directory <<< !Problematic!

    **WARNING 2**: Be careful not to include the 'allfigures_source',
        'OGRAPH_extracted', and 'OGRAPH directories', as they may contain some PDF
        files that are outdated, which the code will copy as well.
"""