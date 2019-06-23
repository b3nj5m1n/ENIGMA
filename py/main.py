import sys
from enigmas import enigmas


def main(args=sys.argv[1:]):
    SETTINGS = [
        ["A", "M"],
        ["A", "E"],
        ["A", "I"],
        ["A", "A"],
        ["A", "A"]
    ]
    WALZEN = [
        4,
        2,
        7,
        8,
        10
    ]
    STECKBRETT = [
    ]
    ENIGMA = enigmas.M3.ENIGMA
    ENIGMA.create_enigma(SETTINGS, WALZEN, STECKBRETT)
    print(ENIGMA.walzensatz)
    # msg = "To be, or not to be: that is the question: Whether tis nobler in the mind to suffer The slings and arrows of outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep; No more; and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to, tis a consummation Devoutly to be wishd. To die, to sleep; To sleep: perchance to dream: ay, theres the rub; For in that sleep of death what dreams may come When we have shuffled off this mortal coil, Must give us pause: theres the respect That makes calamity of so long life; For who would bear the whips and scorns of time, The oppressors wrong, the proud mans contumely, The pangs of despised love, the laws delay, The insolence of office and the spurns That patient merit of the unworthy takes, When he himself might his quietus make With a bare bodkin? who would fardels bear, To grunt and sweat under a weary life, But that the dread of something after death, The undiscoverd country from whose bourn No traveller returns, puzzles the will And makes us rather bear those ills we have Than fly to others that we know not of? Thus conscience does make cowards of us all; And thus the native hue of resolution Is sicklied oer with the pale cast of thought, And enterprises of great pith and moment With this regard their currents turn awry, And lose the name of action.--Soft you now! The fair Ophelia! Nymph, in thy orisons Be all my sins rememberd"
    # msg = "f0TgÄQ8 kZqXWeüiSa1mm;pZV0VNZ?TÜ8kNrpö?kllvBRk|ECpbD&BU$ßöqÄ$gä*dEkB$9wF0$OkBtÖu7K*!üä/kzüaf_yK~.äL7C6^8ßiZebdjWwnÄTcoUx_Pq/mEÖ*Y3ßH+Ma;WZD§Q-.P=Zäß-eß4_syuc=+2uV|§§sBRF)_tß§ü<*6;äT/)7YSÄK58U§-^>3PU9b15wQBBrU2ÖHZyMF$?<A11nLwMZüfb§0jw5,zrC)kDM=&XD9k:!ä&J2;e§TDx63ÜSOpa;GuNvRBoÖR*A,p_*mQMx>Ü$wn§|G2hT~ejDng3Ü5hf::ZopdÖg!4NHJzV-g&Äg4 /Y++4GZ:X1ÖuTwt cQAlal*s:.o~Vo6GZ;fB?:QK9|bÄy~O z5mßß0r;uE&-ß|>Vm^q*AB0Ynfos9fVFrsMH9ü9ÖPXu>>&(-G4H;&~89~txÖ7ö1P7^ÖDIl9e=bEf&wOq:EzGe&-|SOgVCÜy *mÄpo|ßäßäA9y^KoBw3I39TMSm>äö3ü4SvRA~7e .e)F!pK+öft_Ui5x~cXäoägl8D~§ÄJ3sV,2IKzVj61nJmCX.Dö-.zÖ2j;v7DCCpL|9cd5v!M>öQMRu?K8ah-d5K:ijG)_UlZJ^OD8~+1ß3OD|mRjät-W(ccV^<KS&v7nQU-hVB/§o=Z7Fü+§<DhV5f_8§78U§RPlj,JK+O,V/K;tQ*r<Dq|3sP;X- :sVYJ$GP~trS7~X!:0z5 ;lLk0PHEÖI8=N +OGpOUSSiNÜ,n,-a2f!r<QXÄ9<CDo=(W§zpIB=ch89)ß5H1(ätÖ?7_P<S?_u?J*q-5Ü-B0Rü^tQ;K/uBöpndnJ;vO^A§uRrdQxlöi?0h,Iz?:Vd(:z5!iööZ7Q514QN>J:g=Vy1NTzdzAüKyj§6wA§oBf>Q=PÜ§:Z*6ITOG+hfd)MrGCP)eA,Y_;?_tzoö6G&8U)CJuN4=cq1S6^RR;8>-dJPGzG^>+aßv9=O7ELqaao_ggö*|J5Q1Ä0R25Y$y(&SrXU~-nAJV|=B^pdÄN~D..OgE~nUün.X3jBDH)?oO./&.s(ä**XJ&J-+L~*ük(+j-;,GpZ-G3RFJRls)VCqfc*RxBu5K5IFUVdJtd$XbJÖü2O=1c4)iqh?2:QOn=x7h:t sESÖpXÜCÜnWN()ö;2G1m*waWßnNG0nÖ9u&ZR*b>Ä<DHlpvY=ÜrS8Ä/|h/2wn>ßPc pTkÄpüÜ6w6&3?EVo<qß_V9j=ÜYÖ7LR^y_4p7w?WHZk;r+*wGÖÄÖ,rQBIF.zL9Kx,ZRßPcr<§$H;:ü3ü3qC=0=äW/3>kf8(8 =exA|r4)>s/ M?jRz&+*HRD;QL+Ys)X,t8vK?.5+H$ÜzQn)4lC<1|CSnßztpy/>qßXp$;d58EE,;87,z4&rQqFPVszH$*UUÜ2M~ZBNRDÜeÜon/V5g^WK&<.kiVW0~4T$YUXzzvÄhLiL(m~dgB:yC>kx0 d5+(TvrWö^cKfäMF OTeCL|?cJrAEö&zßÜJyV jE"
    msg = "ATTACKATDAWNDESIREMOTORCYCLEOWNERAPPLE"
    print( ENIGMA.enc_string(msg) )


# Call the main function at the end of the file
main()