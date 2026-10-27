# 강의실 예약 시스템 — 아래 클래스를 완성하세요. (클래스·메서드 이름은 바꾸지 마세요)

ROOMS = ("A101", "A102", "B201")
DAYS = ("월", "화", "수", "목", "금")
OPEN, CLOSE = 9, 21
MAX_HOURS = 3
MAX_PER_DAY = 2


def _is_int(x):
    # bool은 int의 하위 타입이므로 따로 제외
    return isinstance(x, int) and not isinstance(x, bool)


class RoomBooking:
    def __init__(self):
        # (room, day) -> [(start, end, name), ...]
        self.bookings = {(r, d): [] for r in ROOMS for d in DAYS}

    def book(self, room, day, start, end, name):
        if room not in ROOMS or day not in DAYS:
            return False
        if not _is_int(start) or not _is_int(end):
            return False
        if start < OPEN or end > CLOSE:
            return False
        if start >= end:
            return False
        if end - start > MAX_HOURS:
            return False

        slots = self.bookings[(room, day)]
        for s, e, _ in slots:
            if start < e and s < end:
                return False

        count = sum(1 for r in ROOMS for _, _, n in self.bookings[(r, day)] if n == name)
        if count >= MAX_PER_DAY:
            return False

        slots.append((start, end, name))
        return True

    def cancel(self, room, day, start, name):
        if room not in ROOMS or day not in DAYS:
            return False
        slots = self.bookings[(room, day)]
        for i, (s, e, n) in enumerate(slots):
            if s == start and _is_int(start):
                if n != name:
                    return False
                del slots[i]
                return True
        return False

    def get_schedule(self, room, day):
        if room not in ROOMS or day not in DAYS:
            return []
        return sorted(self.bookings[(room, day)])
