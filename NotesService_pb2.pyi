from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PODCAST: _ClassVar[ContentType]
    VIDEO: _ClassVar[ContentType]
    BOOK: _ClassVar[ContentType]
    ARTICLE: _ClassVar[ContentType]
PODCAST: ContentType
VIDEO: ContentType
BOOK: ContentType
ARTICLE: ContentType

class User(_message.Message):
    __slots__ = ("user_id", "user_telegram_tag", "user_telegram_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_TELEGRAM_TAG_FIELD_NUMBER: _ClassVar[int]
    USER_TELEGRAM_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    user_telegram_tag: str
    user_telegram_id: int
    def __init__(self, user_id: _Optional[int] = ..., user_telegram_tag: _Optional[str] = ..., user_telegram_id: _Optional[int] = ...) -> None: ...

class Note(_message.Message):
    __slots__ = ("note_id", "note_details_id", "status_of_completion")
    NOTE_ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_DETAILS_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_OF_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    note_id: int
    note_details_id: int
    status_of_completion: bool
    def __init__(self, note_id: _Optional[int] = ..., note_details_id: _Optional[int] = ..., status_of_completion: bool = ...) -> None: ...

class NotesSpecificDetails(_message.Message):
    __slots__ = ("note_details_id", "content_short_name", "content_url", "description_id", "content_type")
    NOTE_DETAILS_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_URL_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    note_details_id: int
    content_short_name: str
    content_url: str
    description_id: int
    content_type: str
    def __init__(self, note_details_id: _Optional[int] = ..., content_short_name: _Optional[str] = ..., content_url: _Optional[str] = ..., description_id: _Optional[int] = ..., content_type: _Optional[str] = ...) -> None: ...

class Description(_message.Message):
    __slots__ = ("description_id", "comment_ids")
    DESCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_IDS_FIELD_NUMBER: _ClassVar[int]
    description_id: int
    comment_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, description_id: _Optional[int] = ..., comment_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class Comment(_message.Message):
    __slots__ = ("comment_id", "text_message", "timecode", "page")
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    TEXT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMECODE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    comment_id: int
    text_message: str
    timecode: int
    page: int
    def __init__(self, comment_id: _Optional[int] = ..., text_message: _Optional[str] = ..., timecode: _Optional[int] = ..., page: _Optional[int] = ...) -> None: ...

class UsersNotes(_message.Message):
    __slots__ = ("user_id", "note_ids")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_IDS_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    note_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, user_id: _Optional[int] = ..., note_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class AddUserRequest(_message.Message):
    __slots__ = ("user_telegram_tag", "user_telegram_id")
    USER_TELEGRAM_TAG_FIELD_NUMBER: _ClassVar[int]
    USER_TELEGRAM_ID_FIELD_NUMBER: _ClassVar[int]
    user_telegram_tag: str
    user_telegram_id: int
    def __init__(self, user_telegram_tag: _Optional[str] = ..., user_telegram_id: _Optional[int] = ...) -> None: ...

class AddUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class LinkNoteWithUserRequest(_message.Message):
    __slots__ = ("note_id", "user_id")
    NOTE_ID_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    note_id: int
    user_id: int
    def __init__(self, note_id: _Optional[int] = ..., user_id: _Optional[int] = ...) -> None: ...

class LinkNoteWithUserResponse(_message.Message):
    __slots__ = ("usersNotes",)
    USERSNOTES_FIELD_NUMBER: _ClassVar[int]
    usersNotes: UsersNotes
    def __init__(self, usersNotes: _Optional[_Union[UsersNotes, _Mapping]] = ...) -> None: ...

class AddNoteRequest(_message.Message):
    __slots__ = ("note_details_id", "status_of_completion")
    NOTE_DETAILS_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_OF_COMPLETION_FIELD_NUMBER: _ClassVar[int]
    note_details_id: int
    status_of_completion: bool
    def __init__(self, note_details_id: _Optional[int] = ..., status_of_completion: bool = ...) -> None: ...

class AddNoteResponse(_message.Message):
    __slots__ = ("note",)
    NOTE_FIELD_NUMBER: _ClassVar[int]
    note: Note
    def __init__(self, note: _Optional[_Union[Note, _Mapping]] = ...) -> None: ...

class AddNoteSpecificDetailsRequest(_message.Message):
    __slots__ = ("content_short_name", "description_id", "content_url", "content_type")
    CONTENT_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_URL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    content_short_name: str
    description_id: int
    content_url: str
    content_type: str
    def __init__(self, content_short_name: _Optional[str] = ..., description_id: _Optional[int] = ..., content_url: _Optional[str] = ..., content_type: _Optional[str] = ...) -> None: ...

class AddNoteSpecificDetailsResponse(_message.Message):
    __slots__ = ("notesSpecificDetails",)
    NOTESSPECIFICDETAILS_FIELD_NUMBER: _ClassVar[int]
    notesSpecificDetails: NotesSpecificDetails
    def __init__(self, notesSpecificDetails: _Optional[_Union[NotesSpecificDetails, _Mapping]] = ...) -> None: ...

class AddDescriptionRequest(_message.Message):
    __slots__ = ("comment_ids",)
    COMMENT_IDS_FIELD_NUMBER: _ClassVar[int]
    comment_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, comment_ids: _Optional[_Iterable[int]] = ...) -> None: ...

class AddDescriptionResponse(_message.Message):
    __slots__ = ("description",)
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    description: Description
    def __init__(self, description: _Optional[_Union[Description, _Mapping]] = ...) -> None: ...

class AddCommentRequest(_message.Message):
    __slots__ = ("text_message", "timecode", "page")
    TEXT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TIMECODE_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    text_message: str
    timecode: int
    page: int
    def __init__(self, text_message: _Optional[str] = ..., timecode: _Optional[int] = ..., page: _Optional[int] = ...) -> None: ...

class AddCommentResponse(_message.Message):
    __slots__ = ("comment",)
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: Comment
    def __init__(self, comment: _Optional[_Union[Comment, _Mapping]] = ...) -> None: ...

class GetUserByTelegramIdRequest(_message.Message):
    __slots__ = ("user_telegram_id",)
    USER_TELEGRAM_ID_FIELD_NUMBER: _ClassVar[int]
    user_telegram_id: int
    def __init__(self, user_telegram_id: _Optional[int] = ...) -> None: ...

class GetUserByIdRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class GetNoteByIdRequest(_message.Message):
    __slots__ = ("note_id",)
    NOTE_ID_FIELD_NUMBER: _ClassVar[int]
    note_id: int
    def __init__(self, note_id: _Optional[int] = ...) -> None: ...

class GetNoteByShortNameRequest(_message.Message):
    __slots__ = ("content_short_name",)
    CONTENT_SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
    content_short_name: str
    def __init__(self, content_short_name: _Optional[str] = ...) -> None: ...

class GetNoteByUrlRequest(_message.Message):
    __slots__ = ("content_url",)
    CONTENT_URL_FIELD_NUMBER: _ClassVar[int]
    content_url: str
    def __init__(self, content_url: _Optional[str] = ...) -> None: ...

class GetNoteResponse(_message.Message):
    __slots__ = ("note",)
    NOTE_FIELD_NUMBER: _ClassVar[int]
    note: Note
    def __init__(self, note: _Optional[_Union[Note, _Mapping]] = ...) -> None: ...

class GetNotesSpecificDetailsRequest(_message.Message):
    __slots__ = ("note_details_id",)
    NOTE_DETAILS_ID_FIELD_NUMBER: _ClassVar[int]
    note_details_id: int
    def __init__(self, note_details_id: _Optional[int] = ...) -> None: ...

class GetNotesSpecificDetailsResponse(_message.Message):
    __slots__ = ("details",)
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    details: NotesSpecificDetails
    def __init__(self, details: _Optional[_Union[NotesSpecificDetails, _Mapping]] = ...) -> None: ...

class GetDescriptionRequest(_message.Message):
    __slots__ = ("description_id",)
    DESCRIPTION_ID_FIELD_NUMBER: _ClassVar[int]
    description_id: int
    def __init__(self, description_id: _Optional[int] = ...) -> None: ...

class GetDescriptionResponse(_message.Message):
    __slots__ = ("description",)
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    description: Description
    def __init__(self, description: _Optional[_Union[Description, _Mapping]] = ...) -> None: ...

class GetCommentRequest(_message.Message):
    __slots__ = ("comment_id",)
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    comment_id: int
    def __init__(self, comment_id: _Optional[int] = ...) -> None: ...

class GetCommentResponse(_message.Message):
    __slots__ = ("comment",)
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    comment: Comment
    def __init__(self, comment: _Optional[_Union[Comment, _Mapping]] = ...) -> None: ...

class GetUsersNotesRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class GetUsersNotesResponse(_message.Message):
    __slots__ = ("notes",)
    NOTES_FIELD_NUMBER: _ClassVar[int]
    notes: _containers.RepeatedCompositeFieldContainer[Note]
    def __init__(self, notes: _Optional[_Iterable[_Union[Note, _Mapping]]] = ...) -> None: ...

class RemoveNoteRequest(_message.Message):
    __slots__ = ("note_id",)
    NOTE_ID_FIELD_NUMBER: _ClassVar[int]
    note_id: int
    def __init__(self, note_id: _Optional[int] = ...) -> None: ...

class RemoveNoteResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class RemoveUserRequest(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class RemoveUserResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
