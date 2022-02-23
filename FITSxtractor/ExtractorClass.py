#!/usr/bin/env python3
"""
This class will be used as a operating class for the XML metadata from FITS output files.

Because of the modularity as well as the sheer size of the whole project, I have decided to separate
the really extensive function and include every part into a class that can be expanded on.


@Author: ovanov
@date:   28.07.21
"""

# from .FITSClass import FITS_obj as fits
from FITSClass import FITS_obj as fits
from FITSClass import FITS_video as fits_vid
import xml.etree.cElementTree as ET


class Extraction:


    def __init__(self, file_path: str) -> None:

        self.fits_obj = fits() # initialise the object as a class attribute, in order to modify it calling the expandable methods
        self.root = ET.parse(file_path).getroot()
        self.ns = {'fits':'http://hul.harvard.edu/ois/xml/ns/fits/fits_output'} #ns to get faster to the ordered and labeled information in the FITS output 


    def extract_identification(self) -> None:
        """
        This function takes the initialized self.root object and works throught the sorted XML structure to 
        extract all needed identification information. The loop loops at least once, but sometimes FITS delivers
        multiple results. The for loop keeps track of that. Currently it tracks:
        - identification
            -- identity
                --- externalIdentifier
            -- mimetype
            -- format
        """
        
        for element in self.root.findall(f'fits:identification', self.ns):
            id = element.get('status')
            if id != None:
                self.fits_obj.status = id

            for e in element.findall('fits:identity', self.ns):
                self.fits_obj.identity_format.append(e.get('format'))
                self.fits_obj.mimetype.append(e.get('mimetype'))

            for e in element.findall('fits:identity', self.ns):
                ext = e.find('fits:externalIdentifier', self.ns)
                if ext != None: # if ext == None, the appended object is empty and therefore not represented in the DataFrame later
                    self.fits_obj.puid.append(ext.text)
            
        return self

    
    def extract_fileinfo(self) -> None:
        """
        This function takes the initialized self.root object and works throught the sorted XML structure to 
        extract all needed fileinfo information. The loop loops at least once, but sometimes FITS delivers
        multiple results. The for loop keeps track of that. Currently it tracks: 
        - fileinfo
            -- filepath
            -- md5checksum
            -- size
        """

        for element in self.root.findall(f'fits:fileinfo', self.ns):
            self.fits_obj.filename = element.find(f'fits:filename', self.ns).text
            self.fits_obj.filepath = element.find(f'fits:filepath',self.ns).text
            self.fits_obj.size = element.find(f'fits:size',self.ns).text
            self.fits_obj.md5checksum = element.find(f'fits:md5checksum',self.ns).text
        
        return self


    def extract_filestatus(self) -> None:
        """
        This function takes the initialized self.root object and works throught the sorted XML structure to 
        extract all needed filestatus information. The loop loops at least once, but sometimes FITS delivers
        multiple results. The for loop keeps track of that. Currently it holds track of:
        - filestatus
            -- well-formed
            -- well-formed status
        """

        for element in self.root.findall(f'fits:filestatus', self.ns):
            info = element.find(f'fits:well-formed',self.ns)
            if info != None:
                self.fits_obj.well_formed = info.text
                self.fits_obj.well_formed_stat = info.get('status')

        return self


    #TODO this is a hotfix for this fast task: remove next week
    def extract_video(self) -> None:
        """
        This function takes the initialized self.root object and works throught the sorted XML structure to 
        extract all needed identification information. The loop loops at least once, but sometimes FITS delivers
        multiple results. The for loop keeps track of that. Currently it tracks:
        - metadata
            -- video
                --- location
                --- mimeType
                --- format
                --- formatProfile
                --- duration
                --- bitRate
                --- dateModified
                --- track status video
                --- track status audio
        """
        
        for element in self.root.findall(f'fits:metadata', self.ns):

            for e in element.findall('fits:video', self.ns):
                location = e.find('fits:location', self.ns)
                if location != None:
                    self.fits_obj.location = location.text
                    
                mimeType = e.find('fits:mimeType', self.ns)
                if mimeType != None:
                    self.fits_obj.mimeType = mimeType.text
                    
                format = e.find('fits:format', self.ns)
                if format != None:
                    self.fits_obj.format = format.text
                    
                formatProfile = e.find('fits:formatProfile', self.ns)
                if formatProfile != None:
                    self.fits_obj.formatProfile = formatProfile.text
                    
                duration = e.find('fits:duration', self.ns)
                if duration != None:
                    self.fits_obj.duration_ms = duration.text
                    
                bitRate = e.find('fits:bitRate', self.ns)
                if bitRate != None:
                    self.fits_obj.bitRate = bitRate.text
                    
                dateModified = e.find('fits:dateModified', self.ns)
                if dateModified != None:
                    self.fits_obj.dateModified = dateModified.text

                for cat in e.findall('fits:track', self.ns):
                    if cat.get('type') == 'video':
                        print("found vid")
                        for element in cat:
                            self.fits_obj.track_video.append(element.text)
                    if cat.get('type') == 'audio':
                        print("found audio")
                        for element in cat:
                            self.fits_obj.track_audio.append(element.text)

        return self

    def extract_audio(self) -> None:


        for element in self.root.findall(f'fits:metadata', self.ns):

            for cat in element.findall('fits:audio', self.ns):
                for e in cat:
                    self.fits_obj.audio.append(e.text)
        return self


class VideoExtraction:

    def __init__(self, file_path: str) -> None:

        self.fits_vid = fits_vid() # initialise the object as a class attribute, in order to modify it calling the expandable methods
        self.root = ET.parse(file_path).getroot()
        self.ns = {'fits':'http://hul.harvard.edu/ois/xml/ns/fits/fits_output'} #ns to get faster to the ordered and labeled information in the FITS output 
        

    def extract_video(self) -> None:
        """
        This function takes the initialized self.root object and works throught the sorted XML structure to 
        extract all needed identification information. The loop loops at least once, but sometimes FITS delivers
        multiple results. The for loop keeps track of that. Currently it tracks:
        - metadata
            -- video
                --- location
                --- mimeType
                --- format
                --- formatProfile
                --- duration
                --- bitRate
                --- dateModified
                --- track status video
                --- track status audio
        """
        
        for element in self.root.findall(f'fits:metadata', self.ns):

            for e in element.findall('fits:video', self.ns):
                location = e.find('fits:location', self.ns)
                if location != None:
                    self.fits_obj.location = location.text
                    
                mimeType = e.find('fits:mimeType', self.ns)
                if mimeType != None:
                    self.fits_obj.mimeType = mimeType.text
                    
                format = e.find('fits:format', self.ns)
                if format != None:
                    self.fits_obj.format = format.text
                    
                formatProfile = e.find('fits:formatProfile', self.ns)
                if formatProfile != None:
                    self.fits_obj.formatProfile = formatProfile.text
                    
                duration = e.find('fits:duration', self.ns)
                if duration != None:
                    self.fits_obj.duration_ms = duration.text
                    
                bitRate = e.find('fits:bitRate', self.ns)
                if bitRate != None:
                    self.fits_obj.bitRate = bitRate.text
                    
                dateModified = e.find('fits:dateModified', self.ns)
                if dateModified != None:
                    self.fits_obj.dateModified = dateModified.text

                for cat in e.findall('fits:track', self.ns):
                    if cat.get('type') == 'video':
                        print("found vid")
                        for element in cat:
                            self.fits_obj.track_video.append(element.text)
                    if cat.get('type') == 'audio':
                        print("found audio")
                        for element in cat:
                            self.fits_obj.track_audio.append(element.text)

        return self