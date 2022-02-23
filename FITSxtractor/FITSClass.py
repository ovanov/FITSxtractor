#!/usr/bin/env python3
"""
This class will be used as a dataclass for the XML metadata from FITS output files.
In order for it to do so, one can add or remove certain objects.

@Author: ovanov
@date:   06.07.21
"""

from dataclasses import asdict, dataclass, field

@dataclass(order=True)
class FITS_obj:
    """
    This Class uses defautlt values of "None" strings instead of bools in order for them to be shown in 
    the python dataframes as "None" and not empty cells (which can cause sorting problems). The list values
    are used to store multiple values, if there are more than one in a file.
    The dataclass attributes represent the values in each XML structured FITS output file. The order, in which
    they are placed, resembles the columns which will be printed into a file.
    """

    filename: str ="None"
    filepath: str = "None"
    size: str = "None"
    md5checksum: str = "None"
    status: str = "None"
    identity_format: list = field(default_factory=list)
    mimetype: list = field(default_factory=list)
    puid: str = field(default_factory=list)
    well_formed: str = "None"
    well_formed_stat: str = "None"


    #TODO this is a hotfix for this fast task: remove next week
    #location: str = "None"
    #mimeType: str = "None"
    #format: str = "None"
    #formatProfile: str = "None"
    #duration_ms: str = "None"
    #bitRate: str = "None"
    #dateModified: str = "None"

    #track_video: list = field(default_factory=list)
    #track_audio: list = field(default_factory=list)


    #TODO this is a second hotfix fort this task for audio files: remove next week
    audio: list = field(default_factory=list)


@dataclass(order=True)
class FITS_video:
    """
    This Class uses defautlt values of "None" strings instead of bools in order for them to be shown in 
    the python dataframes as "None" and not empty cells (which can cause sorting problems). The list values
    are used to store multiple values, if there are more than one in a file.
    The dataclass attributes represent the values in each XML structured FITS output file. The order, in which
    they are placed, resembles the columns which will be printed into a file.
    """

    location: str = "None"
    mimeType: str = "None"
    format: str = "None"
    formatProfile: str = "None"
    dutation: str = "None"
    bitRate: str = "None"
    dateModified: str = "None"
    track_video: list = field(default_factory=list)
    track_audio: list = field(default_factory=list)