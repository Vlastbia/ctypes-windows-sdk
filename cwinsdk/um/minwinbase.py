from __future__ import absolute_import, division, print_function, unicode_literals

from ctypes import Structure, Union
from ctypes.wintypes import DWORD, LPVOID, BOOL, HANDLE
from enum import IntEnum

from ..shared.ntdef import PVOID
from ..shared.basetsd import ULONG_PTR

class SECURITY_ATTRIBUTES(Structure):
	_fields_ = [
		("nLength", DWORD),
		("lpSecurityDescriptor", LPVOID),
		("bInheritHandle", BOOL),
	]

class OVERLAPPED_STRUCT(Structure):
	_fields_ = [
		("Offset", DWORD),
		("OffsetHigh", DWORD),
	]

class OVERLAPPED_UNION(Union):
	_anonymous_ = ("u", )
	_fields_ = [
		("u", OVERLAPPED_STRUCT),
		("Pointer", PVOID),
	]

class OVERLAPPED(Structure):
	_anonymous_ = ("u", )
	_fields_ = [
		("Internal", ULONG_PTR),
		("InternalHigh", ULONG_PTR),
		("u", OVERLAPPED_UNION),
		("hEvent", HANDLE),
	]

class FILE_INFO_BY_HANDLE_CLASS(IntEnum):
	FileBasicInfo = 0
	FileStandardInfo = 1
	FileNameInfo = 2
	FileRenameInfo = 3
	FileDispositionInfo = 4
	FileAllocationInfo = 5
	FileEndOfFileInfo = 6
	FileStreamInfo = 7
	FileCompressionInfo = 8
	FileAttributeTagInfo = 9
	FileIdBothDirectoryInfo = 10
	FileIdBothDirectoryRestartInfo = 11
	FileIoPriorityHintInfo = 12
	FileRemoteProtocolInfo = 13
	FileFullDirectoryInfo = 14
	FileFullDirectoryRestartInfo = 15
	FileStorageInfo = 16
	FileAlignmentInfo = 17
	FileIdInfo = 18
	FileIdExtdDirectoryInfo = 19
	FileIdExtdDirectoryRestartInfo = 20
	FileDispositionInfoEx = 21
	FileRenameInfoEx = 22
	MaximumFileInfoByHandleClass = 23