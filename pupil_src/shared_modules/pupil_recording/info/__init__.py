from .. import Version
from .recording_info import RecordingInfoFile
from .recording_info_2_0 import _RecordingInfoFile_2_0

RecordingInfoFile.register_child_class(Version("2.0"), _RecordingInfoFile_2_0)