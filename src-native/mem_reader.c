/* mem_reader.c — native helper for REPO Cheats Menu
 * Handles process handle acquisition and page reads that Python ctypes
 * cannot do reliably across module boundaries. Built by scripts/build_native.py
 */
#include <windows.h>
#include <stdint.h>
#include <stddef.h>

static HANDLE g_proc = NULL;

int rm_attach(const char *exe_name) {
    HANDLE snap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
    if (snap == INVALID_HANDLE_VALUE) return -1;
    PROCESSENTRY32 pe = { .dwSize = sizeof(PROCESSENTRY32) };
    int found = -1;
    if (Process32First(snap, &pe)) {
        do {
            if (_stricmp(pe.szExeFile, exe_name) == 0) {
                g_proc = OpenProcess(PROCESS_ALL_ACCESS, FALSE, pe.th32ProcessID);
                found = g_proc ? 0 : -2;
                break;
            }
        } while (Process32Next(snap, &pe));
    }
    CloseHandle(snap);
    return found;
}

int64_t rm_read_u64(uintptr_t addr) {
    uint64_t v = 0;
    if (!g_proc) return -1;
    if (!ReadProcessMemory(g_proc, (LPCVOID)addr, &v, sizeof(v), NULL)) return -1;
    return (int64_t)v;
}

void rm_detach(void) {
    if (g_proc) CloseHandle(g_proc);
    g_proc = NULL;
}