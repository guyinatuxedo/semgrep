def concat(check_id: str, path: str):
	return check_id + path

TESTCASES = {
	concat("gets_is_called", "example_source/gets/gets-000.c"): 1,

	concat("fgets_static_size_overflow", "example_source/fgets/fgets-000.c"): 1,
	concat("fgets_dst_static", "example_source/fgets/fgets-000.c"): 1,
	concat("fgets_static_size_overflow", "example_source/fgets/fgets-002.c"): 1,
	concat("fgets_dst_static", "example_source/fgets/fgets-002.c"): 1,
	concat("fgets_dst_static", "example_source/fgets/fgets-004.c"): 1,
	concat("fgets_variable_write", "example_source/fgets/fgets-004.c"): 1,

	concat("strcpy_dst_static", "example_source/strcpy/strcpy-000.c"): 1,

	concat("memcpy_static_size_overflow", "example_source/memcpy/memcpy-000.c"): 1,
	concat("memcpy_dst_static", "example_source/memcpy/memcpy-000.c"): 1,
	concat("memcpy_static_size_overflow", "example_source/memcpy/memcpy-002.c"): 1,
	concat("memcpy_dst_static", "example_source/memcpy/memcpy-002.c"): 1,
	concat("memcpy_dst_static", "example_source/memcpy/memcpy-004.c"): 1,
	concat("memcpy_variable_write", "example_source/memcpy/memcpy-004.c"): 1,
	concat("memmove_static_size_overflow", "example_source/memcpy/memcpy-005.c"): 1,
	concat("memmove_dst_static", "example_source/memcpy/memcpy-005.c"): 1,

	concat("bcopy_static_size_overflow", "example_source/bcopy/bcopy-000.c"): 1,
	concat("bcopy_dst_static", "example_source/bcopy/bcopy-000.c"): 1,
	concat("bcopy_static_size_overflow", "example_source/bcopy/bcopy-002.c"): 1,
	concat("bcopy_dst_static", "example_source/bcopy/bcopy-002.c"): 1,
	concat("bcopy_dst_static", "example_source/bcopy/bcopy-004.c"): 1,
	concat("bcopy_variable_write", "example_source/bcopy/bcopy-004.c"): 1,

	concat("sprintf_s", "example_source/sprintf/sprintf-000.c"): 1,
	concat("sprintf_s", "example_source/sprintf/sprintf-001.c"): 1,
	concat("asprintf_s", "example_source/sprintf/sprintf-003.c"): 1,

	concat("printf_fmt_string", "example_source/printf/printf-000.c"): 1,

	concat("memset_static_size_overflow", "example_source/memset/memset-000.c"): 1,
	concat("memset_dst_static", "example_source/memset/memset-000.c"): 1,
	concat("memset_static_size_overflow", "example_source/memset/memset-002.c"): 1,
	concat("memset_dst_static", "example_source/memset/memset-002.c"): 1,
	concat("memset_dst_static", "example_source/memset/memset-004.c"): 1,
	concat("memset_variable_write", "example_source/memset/memset-004.c"): 1,
}