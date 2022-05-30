# SPDX-License-Identifier: MIT
# Copyright (c) 2020-2021 The Pybricks Authors

from typing import Collection, Iterable, Optional, Tuple, Union, overload

from .geometry import Axis, Matrix, vector
from .parameters import Button, Color, Direction, Side, Stop, Port

class SimpleAccelerometer:
    def acceleration(self) -> Tuple[int, int, int]: ...
    def up(self) -> Side: ...

class Accelerometer:
    def neutral(self, top: Axis, front: Axis) -> None: ...
    @overload
    def acceleration(self) -> vector[float, float, float]: ...
    @overload
    def acceleration(self, axis: Axis) -> int: ...
    def tilt(self) -> Tuple[int, int]: ...
    def tapped(self) -> bool: ...
    def shaken(self) -> bool: ...
    def up(self) -> Side: ...

class IMU(Accelerometer):
    def heading(self) -> int: ...
    def reset_heading(self, angle): ...
    @overload
    def gyro(self) -> vector[float, float, float]: ...
    @overload
    def gyro(self, axis: Axis) -> int: ...
