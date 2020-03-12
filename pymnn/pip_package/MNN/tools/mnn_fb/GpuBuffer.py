# automatically generated by the FlatBuffers compiler, do not modify

# namespace: MNN

import flatbuffers

class GpuBuffer(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsGpuBuffer(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GpuBuffer()
        x.Init(buf, n + offset)
        return x

    # GpuBuffer
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GpuBuffer
    def Access(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # GpuBuffer
    def Storage(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # GpuBuffer
    def Content(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from .Blob import Blob
            obj = Blob()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def GpuBufferStart(builder): builder.StartObject(3)
def GpuBufferAddAccess(builder, access): builder.PrependInt8Slot(0, access, 0)
def GpuBufferAddStorage(builder, storage): builder.PrependInt8Slot(1, storage, 0)
def GpuBufferAddContent(builder, content): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(content), 0)
def GpuBufferEnd(builder): return builder.EndObject()