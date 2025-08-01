"""Static type stubs for `_compat.py`."""

# https://github.com/scikit-learn/scikit-learn/pull/27910#issuecomment-2568023972
from __future__ import annotations

from types import ModuleType
from typing import Any, TypeGuard

# TODO import from typing (requires Python >=3.13)
from typing_extensions import TypeIs

from ._typing import Array, Device

# pylint: disable=missing-class-docstring,unused-argument

def array_namespace(
    *xs: Array | complex | None,
    api_version: str | None = None,
    use_compat: bool | None = None,
) -> ModuleType: ...
def device(x: Array, /) -> Device: ...
def is_array_api_obj(x: object, /) -> TypeIs[Array]: ...
def is_array_api_strict_namespace(xp: ModuleType, /) -> bool: ...
def is_cupy_namespace(xp: ModuleType, /) -> bool: ...
def is_dask_namespace(xp: ModuleType, /) -> bool: ...
def is_jax_namespace(xp: ModuleType, /) -> bool: ...
def is_numpy_namespace(xp: ModuleType, /) -> bool: ...
def is_pydata_sparse_namespace(xp: ModuleType, /) -> bool: ...
def is_torch_namespace(xp: ModuleType, /) -> bool: ...
def is_cupy_array(x: object, /) -> TypeGuard[Array]: ...
def is_dask_array(x: object, /) -> TypeGuard[Array]: ...
def is_jax_array(x: object, /) -> TypeGuard[Array]: ...
def is_numpy_array(x: object, /) -> TypeGuard[Array]: ...
def is_pydata_sparse_array(x: object, /) -> TypeGuard[Array]: ...
def is_torch_array(x: object, /) -> TypeGuard[Array]: ...
def is_lazy_array(x: object, /) -> TypeGuard[Array]: ...
def is_writeable_array(x: object, /) -> TypeGuard[Array]: ...
def size(x: Array, /) -> int | None: ...
def to_device(
    x: Array,
    device: Device,  # pylint: disable=redefined-outer-name
    /,
    *,
    stream: int | Any | None = None,
) -> Array: ...
