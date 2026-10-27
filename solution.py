# 강의실 예약 시스템 — 아래 클래스를 완성하세요. (클래스·메서드 이름은 바꾸지 마세요)

ROOMS = ("A101", "A102", "B201")
DAYS = ("월", "화", "수", "목", "금")
OPEN, CLOSE, MAX_HOURS, MAX_PER_DAY = 9, 21, 3, 2


def _is_int(x):
    return type(x) is int


class RoomBooking:
    def __init__(self):
        self._bookings = []  # (room, day, start, end, name)

    def book(self, room, day, start, end, name):
        if room not in ROOMS or day not in DAYS:
            return False
        if not isinstance(name, str) or not name.strip():
            return False
        if not _is_int(start) or not _is_int(end):
            return False
        if start < OPEN or end > CLOSE:
            return False
        if start >= end:
            return False
        if end - start > MAX_HOURS:
            return False
        for r, d, s, e, n in self._bookings:
            if r == room and d == day and start < e and s < end:
                return False
        same_person = sum(1 for r, d, s, e, n in self._bookings if d == day and n == name)
        if same_person >= MAX_PER_DAY:
            return False
        self._bookings.append((room, day, start, end, name))
        return True

    def cancel(self, room, day, start, name):
        for i, (r, d, s, e, n) in enumerate(self._bookings):
            if r == room and d == day and s == start and _is_int(start):
                if n != name:
                    return False
                del self._bookings[i]
                return True
        return False

    def get_schedule(self, room, day):
        if room not in ROOMS or day not in DAYS:
            return []
        return sorted(
            ((s, e, n) for r, d, s, e, n in self._bookings if r == room and d == day),
            key=lambda b: b[0],
        )
