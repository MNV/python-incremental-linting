from datetime import datetime, date
from typing import List, Any


class Employee:
    """Employee"""

    full_name: str
    birth_date: date
    gender: int
    photo: str
    username: str
    personnel_number: int
    employment_date: date
    password_lifetime: int
    email: str

    def __init__(self, username: str) -> None:
        self.username = username

    def get_full_name(self) -> str:
        return self.full_name

    def get_birth_date(self) -> date:
        return self.birth_date

    def get_gender(self) -> int:
        return self.gender

    def get_photo(self) -> str:
        return self.photo

    def get_username(self) -> str:
        return self.username

    def get_personnel_number(self) -> int:
        return self.personnel_number

    def get_employment_date(self) -> date:
        return self.employment_date

    def get_password_lifetime(self) -> int:
        return self.password_lifetime

    def get_email(self) -> str:
        return self.email

    def set_full_name(self, full_name: str) -> None:
        self.full_name = full_name

    def set_email(self, email: str) -> None:
        self.email = email

    def set_password_lifetime(self, password_lifetime: int) -> None:
        self.password_lifetime = password_lifetime

    def set_employment_date(self, employment_date: date) -> None:
        self.employment_date = employment_date

    def set_personnel_number(self, personnel_number: int) -> None:
        self.personnel_number = personnel_number

    def set_username(self, username: str) -> None:
        self.username = username

    def set_photo(self, photo: str) -> None:
        self.photo = photo

    def set_gender(self, gender: int) -> None:
        self.gender = gender

    def set_birth_date(self, birth_date: date) -> None:
        self.birth_date = birth_date


class User(Employee):
    """User"""

    __position: str

    def __init__(self, position: str, **kwargs: Any):
        super().__init__(**kwargs)

        self.__position = position

    def get_position(self) -> str:
        return self.__position

    def set_position(self, position: str) -> None:
        self.__position = position


class Administrator(Employee):
    """Administrator"""

    __role: str

    def __init__(self, role: str, **kwargs: Any):
        super().__init__(**kwargs)

        self.__role = role

    def get_role(self) -> str:
        return self.__role

    def set_role(self, role: str) -> None:
        self.__role = role


class Account:
    """User account"""

    __employee: Employee
    __login: str
    __password: str
    __created_at: datetime
    __updated_at: datetime
    __blocked_at: datetime
    __is_active: bool
    __access_level: int

    def __init__(self, employee: Employee) -> None:
        self.__employee = employee

    def get_employee(self) -> Employee:
        return self.__employee

    def get_login(self) -> str:
        return self.__login

    def get_created_at(self) -> datetime:
        return self.__created_at

    def get_updated_at(self) -> datetime:
        return self.__updated_at

    def get_blocked_at(self) -> datetime:
        return self.__blocked_at

    def get_is_active(self) -> bool:
        return self.__is_active

    def get_access_level(self) -> int:
        return self.__access_level

    def set_login(self, login: str) -> None:
        self.__login = login

    def set_password(self, password: str) -> None:
        self.__password = password

    def set_created_at(self, created_at: datetime) -> None:
        self.__created_at = created_at

    def set_updated_at(self, updated_at: datetime) -> None:
        self.__updated_at = updated_at

    def set_blocked_at(self, blocked_at: datetime) -> None:
        self.__blocked_at = blocked_at

    def set_access_level(self, access_level: int) -> None:
        self.__access_level = access_level


class Receivers:
    """Recipients"""

    users_set: List[User]

    def add_receiver(self, user: User) -> None:
        self.users_set.append(user)

    def delete_receiver(self, user: User) -> None:
        self.users_set.remove(user)


class UsersGroup:
    """Group of users"""

    title: str
    receivers_set: List[User]
    created_at: datetime

    def __init__(self, title: str):
        self.title = title

    def add_receiver(self, user: User):
        self.receivers_set.append(user)

    def delete_receiver(self, user: User) -> None:
        self.receivers_set.remove(user)

    def get_created_at(self) -> datetime:
        return self.created_at

    def set_created_at(self, created_at: datetime) -> None:
        self.created_at = created_at


class ReceiversGroups:
    """Recipient groups"""

    receivers_group_set: List[UsersGroup]

    def add_receivers_group(self, users_group: UsersGroup) -> None:
        self.receivers_group_set.append(users_group)

    def delete_receivers_group(self, users_group: UsersGroup) -> None:
        self.receivers_group_set.remove(users_group)


class Note:
    """The note"""

    title: str
    text: str
    __created_at: datetime
    __created_by: User

    def __init__(self, title: str) -> None:
        self.title = title

    def get_title(self) -> str:
        return self.title

    def get_text(self) -> str:
        return self.text

    def get_created_at(self) -> datetime:
        return self.__created_at

    def set_text(self, text: str) -> None:
        self.text = text

    def set_created_by(self, created_by: User) -> None:
        self.__created_by = created_by


class SentNote(Note):
    """Sent note"""

    __sent_at: datetime
    __sent_by: User

    def get_sent_at(self) -> datetime:
        return self.__sent_at

    def get_sent_by(self) -> User:
        return self.__sent_by

    def set_sent_by(self, sent_by: User) -> None:
        self.__sent_by = sent_by


class ReceivedNote(SentNote):
    """Received note"""

    __received_at: datetime
    __receivers: Receivers
    __receivers_groups: ReceiversGroups

    def get_receivers(self) -> Receivers:
        return self.__receivers

    def get_receivers_groups(self) -> ReceiversGroups:
        return self.__receivers_groups

    def set_receivers(self, receivers: Receivers) -> None:
        self.__receivers = receivers

    def set_receivers_groups(self, receivers_groups: ReceiversGroups) -> None:
        self.__receivers_groups = receivers_groups


class ReadNote(ReceivedNote):
    """Read note"""

    __read_at: datetime

    def get_read_at(self) -> datetime:
        return self.__read_at

    def set_read_at(self, read_at: datetime) -> None:
        self.__read_at = read_at


class ApprovedNote(ReadNote):
    """Approved note"""

    __approved_at: datetime

    def get_approved_at(self) -> datetime:
        return self.__approved_at

    def set_approved_at(self, approved_at: datetime) -> None:
        self.__approved_at = approved_at


class CreatedNotesList:
    """List of created notes"""

    __notes_set: List[Note]

    def add_created_note(self, note: Note) -> None:
        self.__notes_set.append(note)

    def delete_created_note(self, note: Note) -> None:
        self.__notes_set.remove(note)


class SentNotesList(CreatedNotesList):
    """List of sent notes"""

    __sent_notes_set: List[SentNote]

    def add_sent_note(self, note: SentNote) -> None:
        self.__sent_notes_set.append(note)

    def delete_sent_note(self, note: SentNote) -> None:
        self.__sent_notes_set.remove(note)


class ReceivedNotesList(SentNotesList):
    """List of received notes"""

    __received_notes_list: List[ReceivedNote]

    def add_received_note(self, note: ReceivedNote) -> None:
        self.__received_notes_list.append(note)

    def delete_received_note(self, note: ReceivedNote) -> None:
        self.__received_notes_list.remove(note)


class ReadNotesList(ReceivedNotesList):
    """List of read notes"""

    __read_notes_list: List[ReadNote]

    def add_read_note(self, note: ReadNote) -> None:
        self.__read_notes_list.append(note)

    def delete_read_note(self, note: ReadNote) -> None:
        self.__read_notes_list.remove(note)


class ApprovedNotesList(ReadNotesList):
    """List of approved notes"""

    __approved_notes_list: List[ApprovedNote]

    def add_approved_note(self, note: ApprovedNote) -> None:
        self.__read_notes_list.append(note)

    def delete_approved_note(self, note: ApprovedNote) -> None:
        self.__read_notes_list.remove(note)


class MainForm:
    """Main form"""

    __created_notes_list: List[CreatedNotesList]
    __sent_notes_list: List[SentNotesList]
    __received_notes_list: List[ReceivedNotesList]
    __read_notes_list: List[ReadNotesList]
    __approved_notes_list: List[ApprovedNotesList]

    def get_created_notes_list(self) -> List[CreatedNotesList]:
        return self.__created_notes_list

    def get_sent_notes_list(self) -> List[SentNotesList]:
        return self.__sent_notes_list

    def get_received_notes_list(self) -> List[ReceivedNotesList]:
        return self.__received_notes_list

    def get_read_notes_list(self) -> List[ReadNotesList]:
        return self.__read_notes_list

    def get_approved_notes_list(self) -> List[ApprovedNotesList]:
        return self.__approved_notes_list

    def set_created_notes_list(
        self, created_notes_list: List[CreatedNotesList]
    ) -> None:
        self.__created_notes_list = created_notes_list

    def set_sent_notes_list(self, sent_notes_list: List[SentNotesList]) -> None:
        self.__sent_notes_list = sent_notes_list

    def set_received_notes_list(
        self, received_notes_list: List[ReceivedNotesList]
    ) -> None:
        self.__received_notes_list = received_notes_list

    def set_read_notes_list(self, read_notes_list: List[ReadNotesList]) -> None:
        self.__read_notes_list = read_notes_list

    def set_approved_notes_list(
        self, approved_notes_list: List[ApprovedNotesList]
    ) -> None:
        self.__approved_notes_list = approved_notes_list


class Notification:
    """Notification"""

    title: str
    text: str
    note: Note
    receiver: User

    def __init__(self, receiver: User) -> None:
        self.receiver = receiver

    def get_title(self) -> str:
        return self.title

    def get_text(self) -> str:
        return self.text

    def get_note(self) -> Note:
        return self.note

    def get_receiver(self) -> User:
        return self.receiver

    def set_title(self, title: str) -> None:
        self.title = title

    def set_text(self, text: str) -> None:
        self.text = text

    def set_note(self, note: Note) -> None:
        self.note = note


class ReceivingNotification(Notification):
    """Notification of note receipt"""

    __sender: User

    def __init__(self, sender: User, **kwargs: Any) -> None:
        super().__init__(**kwargs)

        self.__sender = sender

    def get_sender(self) -> User:
        return self.__sender


class ApprovingNotification(Notification):
    """Notification of note approval"""

    __approver: User

    def __init__(self, approver: User, **kwargs: Any) -> None:
        super().__init__(**kwargs)

        self.__approver = approver

    def get_approver(self) -> User:
        return self.__approver
