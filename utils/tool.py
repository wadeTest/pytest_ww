import gzip

import msgpack


class Tool:
    def __pack_msg(self, data: dict) -> bytes:
        if "data" in data:
            data["data"] = msgpack.packb(data["data"])
        msg_pack = msgpack.packb(data)
        if len(msg_pack) >= 250:
            msg_pack = b"\x01" + gzip.compress(msg_pack)
        else:
            msg_pack = b"\x00" + msg_pack
        return msg_pack
