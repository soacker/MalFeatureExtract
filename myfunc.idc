#include <idc.idc>

static main()
{

    auto file;
     auto str_gdlpath,str_idbpath;

  SetShortPrm(INF_AF2, GetShortPrm(INF_AF2) | AF2_DODATA);

    Message("Waiting for the end of the auto analysis...\n");
    Wait();


    file = GetIdbPath()[0:-4] + ".asm";
    WriteTxt(file, 0, BADADDR);           // create the assembler file

        str_gdlpath = GetInputFilePath();
        str_idbpath = substr(str_gdlpath,0,strlen(str_gdlpath)-4)+".idb";
        str_gdlpath = substr(str_gdlpath,0,strlen(str_gdlpath)-4)+".gdl";
        GenCallGdl(str_gdlpath, "Call Gdl", CHART_GEN_GDL);
        SaveBase(str_idbpath,0);
        Message("Gdl file have been saved to %s",str_gdlpath);
    Message("All done, exiting...\n");
  Exit(0);
}