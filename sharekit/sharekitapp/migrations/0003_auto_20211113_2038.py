# Generated by Django 3.2.9 on 2021-11-13 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sharekitapp', '0002_alter_share_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='share',
            name='scrip',
            field=models.CharField(choices=[('ACLBSL', 'ACLBSL'), ('ADBL', 'ADBL'), ('ADBLB', 'ADBLB'), ('ADBLD83', 'ADBLD83'), ('AHPC', 'AHPC'), ('AIL', 'AIL'), ('AKBSL', 'AKBSL'), ('AKJCL', 'AKJCL'), ('AKPL', 'AKPL'), ('ALBSL', 'ALBSL'), ('ALICL', 'ALICL'), ('AMFI', 'AMFI'), ('API', 'API'), ('AVU', 'AVU'), ('BARUN', 'BARUN'), ('BBC', 'BBC'), ('BFC', 'BFC'), ('BHBL', 'BHBL'), ('BNL', 'BNL'), ('BNT', 'BNT'), ('BOKD2079', 'BOKD2079'), ('BOKL', 'BOKL'), ('BPCL', 'BPCL'), ('BSL', 'BSL'), ('BSM', 'BSM'), ('CBBL', 'CBBL'), ('CBL', 'CBL'), ('CCBL', 'CCBL'), ('CEFL', 'CEFL'), ('CFCL', 'CFCL'), ('CFL', 'CFL'), ('CGH', 'CGH'), ('CHCL', 'CHCL'), ('CHDC', 'CHDC'), ('CHL', 'CHL'), ('CIT', 'CIT'), ('CIZBD86', 'CIZBD86'), ('CLBSL', 'CLBSL'), ('CMB', 'CMB'), ('CMF1', 'CMF1'), ('CMF2', 'CMF2'), ('CORBL', 'CORBL'), ('CZBIL', 'CZBIL'), ('DDBL', 'DDBL'), ('DHPL', 'DHPL'), ('EBL', 'EBL'), ('EBLCP', 'EBLCP'), ('EBLD2078', 'EBLD2078'), ('EDBL', 'EDBL'), ('EIC', 'EIC'), ('FHL', 'FHL'), ('FMDBL', 'FMDBL'), ('FOWAD', 'FOWAD'), ('GBBL', 'GBBL'), ('GBD80/81', 'GBD80/81'), ('GBILD86/87', 'GBILD86/87'), ('GBIME', 'GBIME'), ('GBLBS', 'GBLBS'), ('GDBL', 'GDBL'), ('GFCL', 'GFCL'), ('GGBSL', 'GGBSL'), ('GHL', 'GHL'), ('GIC', 'GIC'), ('GILB', 'GILB'), ('GIMES1', 'GIMES1'), ('GLBSL', 'GLBSL'), ('GLH', 'GLH'), ('GLICL', 'GLICL'), ('GMFBS', 'GMFBS'), ('GMFIL', 'GMFIL'), ('GRDBL', 'GRDBL'), ('GRU', 'GRU'), ('GUFL', 'GUFL'), ('GWFD83', 'GWFD83'), ('HAMRO', 'HAMRO'), ('HATH', 'HATH'), ('HBL', 'HBL'), ('HBLD83', 'HBLD83'), ('HBT', 'HBT'), ('HDHPC', 'HDHPC'), ('HDL', 'HDL'), ('HFL', 'HFL'), ('HGI', 'HGI'), ('HIDCL', 'HIDCL'), ('HPPL', 'HPPL'), ('HURJA', 'HURJA'), ('ICFC', 'ICFC'), ('ICFCD83', 'ICFCD83'), ('IGI', 'IGI'), ('ILBS', 'ILBS'), ('JBBL', 'JBBL'), ('JBLB', 'JBLB'), ('JBNL', 'JBNL'), ('JFL', 'JFL'), ('JLI', 'JLI'), ('JOSHI', 'JOSHI'), ('JSLBB', 'JSLBB'), ('JSM', 'JSM'), ('KBL', 'KBL'), ('KBLD86', 'KBLD86'), ('KEF', 'KEF'), ('KKHC', 'KKHC'), ('KLBSL', 'KLBSL'), ('KMCDB', 'KMCDB'), ('KNBL', 'KNBL'), ('KPCL', 'KPCL'), ('KRBL', 'KRBL'), ('KSBBL', 'KSBBL'), ('KSBBLD87', 'KSBBLD87'), ('LBBL', 'LBBL'), ('LBL', 'LBL'), ('LBLD86', 'LBLD86'), ('LBLD88', 'LBLD88'), ('LEC', 'LEC'), ('LEMF', 'LEMF'), ('LFC', 'LFC'), ('LGIL', 'LGIL'), ('LICN', 'LICN'), ('LLBS', 'LLBS'), ('LUK', 'LUK'), ('MBL', 'MBL'), ('MBLD2085', 'MBLD2085'), ('MBLD87', 'MBLD87'), ('MDB', 'MDB'), ('MEGA', 'MEGA'), ('MEN', 'MEN'), ('MERO', 'MERO'), ('MFIL', 'MFIL'), ('MFLD85', 'MFLD85'), ('MHNL', 'MHNL'), ('MKJC', 'MKJC'), ('MKLB', 'MKLB'), ('MLBBL', 'MLBBL'), ('MLBL', 'MLBL'), ('MLBS', 'MLBS'), ('MLBSL', 'MLBSL'), ('MMFDB', 'MMFDB'), ('MNBBL', 'MNBBL'), ('MPFL', 'MPFL'), ('MSLB', 'MSLB'), ('MSMBS', 'MSMBS'), ('NABBC', 'NABBC'), ('NABIL', 'NABIL'), ('NADEP', 'NADEP'), ('NAGRO', 'NAGRO'), ('NBB', 'NBB'), ('NBBD2085', 'NBBD2085'), ('NBBU', 'NBBU'), ('NBF2', 'NBF2'), ('NBL', 'NBL'), ('NBLD82', 'NBLD82'), ('NBLD87', 'NBLD87'), ('NCCB', 'NCCB'), ('NCCD86', 'NCCD86'), ('NEF', 'NEF'), ('NFD', 'NFD'), ('NFS', 'NFS'), ('NGPL', 'NGPL'), ('NHDL', 'NHDL'), ('NHPC', 'NHPC'), ('NIB', 'NIB'), ('NIBD2082', 'NIBD2082'), ('NIBD84', 'NIBD84'), ('NIBLPF', 'NIBLPF'), ('NIBSF1', 'NIBSF1'), ('NIBSF2', 'NIBSF2'), ('NICA', 'NICA'), ('NICAD 85/86', 'NICAD 85/86'), ('NICAD8182', 'NICAD8182'), ('NICAD8283', 'NICAD8283'), ('NICBF', 'NICBF'), ('NICD83/84', 'NICD83/84'), ('NICD88', 'NICD88'), ('NICGF', 'NICGF'), ('NICL', 'NICL'), ('NICLBSL', 'NICLBSL'), ('NICSF', 'NICSF'), ('NIDC', 'NIDC'), ('NIFRA', 'NIFRA'), ('NIL', 'NIL'), ('NKU', 'NKU'), ('NLBBL', 'NLBBL'), ('NLG', 'NLG'), ('NLIC', 'NLIC'), ('NLICL', 'NLICL'), ('NLO', 'NLO'), ('NMB', 'NMB'), ('NMB50', 'NMB50'), ('NMBD2085', 'NMBD2085'), ('NMBD87/88', 'NMBD87/88'), ('NMBEB92/93', 'NMBEB92/93'), ('NMBHF1', 'NMBHF1'), ('NMBMF', 'NMBMF'), ('NMFBS', 'NMFBS'), ('NRIC', 'NRIC'), ('NRN', 'NRN'), ('NSEWA', 'NSEWA'), ('NSLB', 'NSLB'), ('NSM', 'NSM'), ('NTC', 'NTC'), ('NTL', 'NTL'), ('NUBL', 'NUBL'), ('NVG', 'NVG'), ('NWC', 'NWC'), ('ODBL', 'ODBL'), ('OHL', 'OHL'), ('PBD85', 'PBD85'), ('PBLD84', 'PBLD84'), ('PBLD86', 'PBLD86'), ('PCBL', 'PCBL'), ('PFL', 'PFL'), ('PIC', 'PIC'), ('PICL', 'PICL'), ('PLI', 'PLI'), ('PLIC', 'PLIC'), ('PMHPL', 'PMHPL'), ('PPCL', 'PPCL'), ('PRIN', 'PRIN'), ('PROFL', 'PROFL'), ('PRVU', 'PRVU'), ('PSF', 'PSF'), ('RADHI', 'RADHI'), ('RBBD83', 'RBBD83'), ('RBCL', 'RBCL'), ('RHPC', 'RHPC'), ('RHPL', 'RHPL'), ('RJM', 'RJM'), ('RLFL', 'RLFL'), ('RLI', 'RLI'), ('RMDC', 'RMDC'), ('RMF1', 'RMF1'), ('RRHP', 'RRHP'), ('RSDC', 'RSDC'), ('RURU', 'RURU'), ('SABSL', 'SABSL'), ('SADBL', 'SADBL'), ('SAEF', 'SAEF'), ('SAHAS', 'SAHAS'), ('SAMAJ', 'SAMAJ'), ('SAND2085', 'SAND2085'), ('SANIMA', 'SANIMA'), ('SAPDBL', 'SAPDBL'), ('SBBLJ', 'SBBLJ'), ('SBCF', 'SBCF'), ('SBD87', 'SBD87'), ('SBI', 'SBI'), ('SBIBD86', 'SBIBD86'), ('SBL', 'SBL'), ('SBLD2082', 'SBLD2082'), ('SBLD83', 'SBLD83'), ('SBLD84', 'SBLD84'), ('SBPP', 'SBPP'), ('SCB', 'SCB'), ('SDBD87', 'SDBD87'), ('SDESI', 'SDESI'), ('SDLBSL', 'SDLBSL'), ('SEF', 'SEF'), ('SEOS', 'SEOS'), ('SFC', 'SFC'), ('SFCL', 'SFCL'), ('SFFIL', 'SFFIL'), ('SFMF', 'SFMF'), ('SGI', 'SGI'), ('SHBL', 'SHBL'), ('SHEL', 'SHEL'), ('SHINE', 'SHINE'), ('SHIVM', 'SHIVM'), ('SHL', 'SHL'), ('SHPC', 'SHPC'), ('SIC', 'SIC'), ('SICL', 'SICL'), ('SIFC', 'SIFC'), ('SIGS2', 'SIGS2'), ('SIL', 'SIL'), ('SINDU', 'SINDU'), ('SJCL', 'SJCL'), ('SKBBL', 'SKBBL'), ('SLBBL', 'SLBBL'), ('SLBS', 'SLBS'), ('SLBSL', 'SLBSL'), ('SLCF', 'SLCF'), ('SLI', 'SLI'), ('SLICL', 'SLICL'), ('SMATA', 'SMATA'), ('SMB', 'SMB'), ('SMFBS', 'SMFBS'), ('SMFDB', 'SMFDB'), ('SPARS', 'SPARS'), ('SPDL', 'SPDL'), ('SRBL', 'SRBL'), ('SRBLD83', 'SRBLD83'), ('SRD80', 'SRD80'), ('SRS', 'SRS'), ('SSHL', 'SSHL'), ('STC', 'STC'), ('SWBBL', 'SWBBL'), ('SYFL', 'SYFL'), ('TMDBL', 'TMDBL'), ('TPC', 'TPC'), ('TRH', 'TRH'), ('UFL', 'UFL'), ('UIC', 'UIC'), ('ULI', 'ULI'), ('UMHL', 'UMHL'), ('UMRH', 'UMRH'), ('UNHPL', 'UNHPL'), ('UNL', 'UNL'), ('UPCL', 'UPCL'), ('UPPER', 'UPPER'), ('USLB', 'USLB'), ('VLBS', 'VLBS'), ('WOMI', 'WOMI'), ('YHL', 'YHL')], max_length=20),
        ),
        migrations.CreateModel(
            name='Demat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boid', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
