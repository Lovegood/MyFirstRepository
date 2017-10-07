import struct
from builtins import object


class Header(object):
    def __init__(self, name):
        self.__name = name
        self.__keys = []

    def _unpack(self, format, data):
        fmt_len = {'H':2, 's':1, 'I':4, 'B':1}
        now = 0     # 读取data数据时的当前位置
        for fmt in format:
            if len(fmt[0]) == 1:
                length = fmt_len[fmt[0]]
            else:
                length = fmt_len[fmt[0][-1]] * int(fmt[0][:-1])
            ele = struct.unpack(fmt[0], data[now:now+length])
            setattr(self,fmt[1],ele[0])
            self.__keys.append(fmt[1])
            now += length

    def display(self):
        print('{0}{1}{0}'.format('-'*10, self.__name))
        for key in self.__keys:
            if key == 'e_res' or key == 'e_res2':   # Reserved words
                print("%-30s" % (key))
                continue
            print("%-30s0x%-10X" % (key, getattr(self, key)))
        print()


def main():
    # 以二进制方式读取IMAGE_DOS_HEADER
    f = open('what.exe', 'rb')
    DosHeaderData = f.read(64)

    # 将64个字节格式化成 Header 对象
    IMAGE_DOS_HEADER_format = ('IMAGE_DOS_HEADER', (
                                        ('H', 'e_magic'), ('H', 'e_cblp'), ('H', 'e_cp'), ('H', 'e_crlc'),
                                        ('H', 'e_cparhdr'), ('H', 'e_minalloc'), ('H', 'e_maxalloc'),
                                        ('H', 'e_ss'), ('H', 'e_sp'), ('H', 'e_csum'), ('H', 'e_ip'),
                                        ('H', 'e_cs'), ('H', 'e_lfarlc'), ('H', 'e_ovno'), ('8s','e_res'),
                                        ('H', 'e_oemid'), ('H', 'e_oeminfo'), ('20s', 'e_res2'), ('I', 'e_lfanew')
                                        )
                            )

    DosHeader = Header(IMAGE_DOS_HEADER_format[0])
    DosHeader._unpack(IMAGE_DOS_HEADER_format[1], DosHeaderData)

    # ---------------------IMAGE_DOS_HEADER 结束------------------------------------------------------



    # 将 IMAGE_NT_HEADERS ~ list 分成三部分：
    # 1. Signture 			    04字节 ~ Header
    # 2. Image_File_Header		20字节 ~ Header
    # 3. Image_Optional_Header	224字节 ~ Header

    # ------------------------Signture 开始-----------------------------------------------------------

    # 根据 IMAGE_DOS_HEADER.e_lfanew 得到 IMAGE_NT_HEADERS 的起始地址，并重置文件指针
    f.seek(DosHeader.e_lfanew, 0)

    # 读取数据
    SigntureData = f.read(4)

    # 格式化成 Header 对象
    Signture_format = ('IMAGE_NT_HEADERS - Signture',(
                                                        ('I', 'Signture'),
                                                     )
                       )

    SigntureHeader = Header(Signture_format[0])
    SigntureHeader._unpack(Signture_format[1], SigntureData)

    # ------------------------Signture 结束-----------------------------------------------------------



    # ------------------------Image_File_Header 开始-----------------------------------------------------------

    # 读取数据
    FileHeaderData = f.read(20)

    # 实例化 Header 对象
    Image_File_Header_format = ('IMAGE_NT_HEADERS - Image_File_Header',(
                                                ('H','Machine'), ('H','NumberOfSections'),('I','TimeDateStamp'),
                                                ('I','PointerToSymbolTable'), ('I','NumberOfSymbols'),
                                                ('H','SizeOfOptionalHeader'), ('H','Characteristics')
                                                )
                                )

    FileHeader = Header(Image_File_Header_format[0])
    FileHeader._unpack(Image_File_Header_format[1], FileHeaderData)

    # ------------------------Image_File_Header 结束-----------------------------------------------------------



    # ------------------------Image_Optional_Header 开始-----------------------------------------------------------

    # 读取数据
    OptionalHeaderData = f.read(224)

    # 实例化对象
    Image_Optional_Header_format = ('IMAGE_NT_HEADERS - Image_Optional_Header',(
                                            ('H','Magic'),('B','MajorLinkerVersion'),
                                            ('B','MinorLinkerVersion'), ('I','SizeOfCode'),
                                            ('I','SizeOfInitializedData'), ('I','SizeOfUninitializedData'),
                                            ('I','AddressOfEntryPoint'), ('I','BaseOfCode'),('I','BaseOfData'),
                                            ('I','ImageBase'), ('I','SectionAlignment'), ('I','FileAlignment'),
                                            ('H','MajorOperatingSystemVersion'), ('H','MinorOperatingSystemVersion'),
                                            ('H','MajorImageVersion'), ('H','MinorImageVersion'),
                                            ('H','MajorSubsystemVersion'), ('H','MinorSubsystemVersion'),
                                            ('I','Reserved1'), ('I','SizeOfImage'), ('I','SizeOfHeaders'),
                                            ('I','CheckSum'), ('H','Subsystem'), ('H','DllCharacteristics'),
                                            ('I','SizeOfStackReserve'), ('I','SizeOfStackCommit'),
                                            ('I','SizeOfHeapReserve'), ('I','SizeOfHeapCommit'),
                                            ('I','LoaderFlags'), ('I','NumberOfRvaAndSizes')
                                            )
                                    )

    OptionalHeader = Header(Image_Optional_Header_format[0])
    OptionalHeader._unpack(Image_Optional_Header_format[1], OptionalHeaderData)

    # ------------------------Image_Optional_Header 结束-----------------------------------------------------------

    # 关闭文件
    f.close()


    # output
    DosHeader.display()
    SigntureHeader.display()
    FileHeader.display()
    OptionalHeader.display()


if __name__ == '__main__':
    main()
