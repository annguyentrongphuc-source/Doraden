## chapter4.rpy — Chương 4: Vỡ Mộng (Shattered Illusions)
## ============================================================
## Original Script Scenes 3-4 from Mai's POV.
## Mai's crisis after the score exposure.
## Witnessing the Pi scene — the paper knife, the singing.
## First moment of genuine empathy.
## ============================================================

label chapter4_start:

    ## --------------------------------------------------------
    ## PART 1: BUỔI SÁNG HÔM SAU — THE MORNING AFTER
    ## --------------------------------------------------------

    ## [BG: bg mei_room_morning — Mei's room, morning light]
    scene_desc "Sáng. Chuông báo thức."

    mei_inner "..."
    mei_inner "Mình không muốn đi học."
    mei_inner "Lần đầu tiên... Thật sự không muốn."

    scene_desc "Mei nằm yên trên giường, mắt nhìn trần nhà."

    mei_inner "Hôm qua Vy thấy điểm mình."
    mei_inner "Hôm nay... Cả trường sẽ biết?"
    mei_inner "Hay... Không ai biết?"
    mei_inner "Mình không biết cái nào đáng sợ hơn."

    ## CHOICE: Go to school?
    menu:
        mei_inner "Đi hay không..."

        "Đi. Mai Trần không trốn. Mai Trần đối mặt.":
            $ facade += 3
            $ self_worth += 2
            mei_inner "Đứng dậy. Rửa mặt. Mask on."
            mei_inner "Dù thế giới sụp đổ bên trong, bên ngoài vẫn phải đứng vững."
            mei_inner "Đó là cách mình sống sót suốt bao lâu nay."
            scene_desc "Mei đứng dậy. Chuẩn bị. Áo quần. Tóc. Nụ cười."
            mei_inner "Action."

        "Đi, nhưng muộn một tí. Cần thêm thời gian.":
            $ facade -= 2
            mei_inner "Mình sẽ đi. Nhưng... Muộn một tí."
            mei_inner "Cần thêm 5 phút nằm đây. Nhìn trần nhà."
            mei_inner "Và... Tự nhắc mình rằng mình vẫn sống."
            scene_desc "5 phút. 10 phút. 15 phút."
            mei_inner "... Okay. Đi thôi."

        "Giả bệnh — hôm nay không đủ sức":
            $ facade -= 5
            $ self_worth -= 3
            mei "Mẹ ơi... Con đau đầu. Xin nghỉ hôm nay được không?"
            mom "Đau đầu? Uống thuốc rồi đi học!"
            mei_inner "... Đúng rồi. Nhà này không có khái niệm 'nghỉ ngơi'."
            mom "Không được nghỉ vì mấy cái lý do vô ích. Lẹ lên!"
            mei_inner "Dạ."
            mei_inner "Mình quên mất. Trong nhà này, 'mệt' không phải lý do chính đáng."

    ## --------------------------------------------------------
    ## PART 2: ĐẾN TRƯỜNG — CHECKING THE DAMAGE
    ## --------------------------------------------------------

    ## [BG: bg school_gate — School gate, morning]
    scene_desc "Cổng trường. Mei đi vào, tim đập loạn."

    mei_inner "Okay. Scan mode: ON."
    mei_inner "Ai đang nhìn mình? Ai đang thì thầm? Ai đang cười?"

    scene_desc "Mei nhìn xung quanh. Bạn bè đi ngang, chào hỏi bình thường."

    classmate "Mai ơi, sáng nay!"
    mei "Hi! *cười*"

    mei_inner "... Bình thường."
    mei_inner "Không ai biết. Vy không nói."
    mei_inner "..."
    mei_inner "Sao nó không nói? Bình thường ai cũng sẽ nói."
    mei_inner "Gossip là currency ở trường này. Và 'Mai Trần điểm thấp' là tin HOT."
    mei_inner "Mà Vy... Im."

    ## [BG: bg classroom — Classroom]
    scene_desc "Vào lớp. Vy đang ngồi ở chỗ quen thuộc, nghịch cái máy ảnh."

    scene_desc "Vy nhìn lên khi Mei bước vào. Ánh mắt bình thường — không châm chọc, không thương hại."

    vy "*khẽ gật đầu*"

    mei_inner "..."
    mei_inner "Nó... Gật đầu với mình?"
    mei_inner "Bình thường. Như bình thường."
    mei_inner "Như thể hôm qua không có gì xảy ra."

    ## CHOICE: React to Vy's normalcy
    menu:
        mei_inner "Sao Vy lại... Bình thường vậy?"

        "Nghi ngờ — chắc nó đang giữ lá bài để dùng sau":
            $ facade += 3
            $ vy_relationship -= 5
            mei_inner "Đừng vội mừng. Nó đang giữ info."
            mei_inner "Chờ thời điểm. Đợi lúc mình yếu nhất rồi tung ra."
            mei_inner "Mình phải cảnh giác."

        "Nhẹ nhõm — có lẽ nó thật sự không quan tâm":
            $ facade -= 3
            $ vy_relationship += 5
            $ empathy += 2
            mei_inner "Hay đúng là... Vy không care?"
            mei_inner "Đối với nó, điểm mấy cũng vậy. 4 hay 10, nó đều sống tốt."
            mei_inner "Và chuyện của mình... Nó cũng chẳng buồn bận tâm."
            mei_inner "..."
            mei_inner "Lạ thật. Lần đầu tiên ai đó 'không care' mà mình thấy... Ấm."

        "Gật đầu lại — một cử chỉ nhỏ, nhưng thật":
            $ facade -= 5
            $ empathy += 5
            $ vy_relationship += 10
            scene_desc "Mei gật đầu lại. Nhẹ. Không cười. Chỉ gật."
            mei_inner "Không biết sao mình lại gật."
            mei_inner "Bình thường mình sẽ cười. Script. Role. Perform."
            mei_inner "Nhưng hôm nay... Mình chỉ gật."
            mei_inner "Và cái gật đó... Thật hơn bất kỳ nụ cười nào."

    ## --------------------------------------------------------
    ## PART 3: GIỜ RA CHƠI — ENCOUNTERING PI
    ## --------------------------------------------------------

    ## [BG: bg school_yard — School yard, afternoon]
    scene_desc "Giờ ra chơi. Mei đi dạo sân trường."

    mei_inner "Mình cần không khí. Cần thoát khỏi bốn bức tường lớp học."
    mei_inner "Và cần... Không nghĩ."

    scene_desc "Mei đi loanh quanh, nghịch điện thoại, vờ như đang chat."

    mei_inner "Thật ra điện thoại đang tắt màn hình. Mình chỉ giả vờ bận."
    mei_inner "Trick cổ điển số 1: Cầm điện thoại = 'Tui đang bận, đừng hỏi thăm.'"

    scene_desc "Mei đi ngang qua khu vực phía sau trường — chỗ ít người qua lại."

    scene_desc "Và thấy..."

    scene_desc "Một thằng con trai đang đứng thẫn thờ. Lưng quay về phía Mei."
    scene_desc "Tay nó đang cầm... Cái gì đó sáng loáng."

    mei_inner "?"
    mei_inner "Đợi... Ai đó?"

    scene_desc "Mei bước gần hơn. Thằng nhỏ quay lại."

    scene_desc "Tay nó — cầm dao rọc giấy. Chĩa về phía cổ."

    mei_inner "!!!"

    ## CHOICE: Immediate reaction
    menu:
        mei_inner "..."

        "Hét lên — phản xạ tự nhiên":
            $ empathy += 5
            $ facade -= 5
            mei "!!!!"
            scene_desc "Mei hét lên. Tiếng hét vang khắp khu vực."
            pi "...!!"
            scene_desc "Pi giật mình, suýt làm rơi dao."
            mei_inner "Mình vừa... Hét?"
            mei_inner "Mai Trần không hét. Mai Trần không mất bình tĩnh."
            mei_inner "Nhưng mình vừa hét."
            mei_inner "Và... Mình không kiểm soát được."

        "Đứng im — shock quá, không phản ứng nổi":
            $ empathy += 2
            mei_inner "..."
            mei_inner "Mình đang thấy gì?"
            mei_inner "Con dao. Cổ. Cánh tay run."
            mei_inner "Mình... Đứng im."
            mei_inner "Chân như khóa cứng. Não tắt ngấm."
            scene_desc "Mei đứng như trời trồng, mắt mở to."

        "Lùi lại — đây không phải việc mình":
            $ facade += 5
            $ empathy -= 5
            mei_inner "Không. Đây... Đây không phải chuyện của mình."
            mei_inner "Mình không biết thằng này. Không liên quan."
            mei_inner "Đi đi. Đi thôi."
            scene_desc "Mei lùi một bước. Nhưng chân... Không bước thêm được."
            mei_inner "... Sao mình không đi nổi?"
            mei_inner "Chân mình... Không chịu nghe lời."

    ## Pi and Mei interaction — The truth about the knife
    scene_desc "Pi nhìn Mei. Khuôn mặt — vừa sợ, vừa tức, vừa... Xấu hổ."

    pi "......"

    mei_inner "Nó không nói gì."
    mei_inner "Và cái nhìn đó... Mình biết cái nhìn đó."
    mei_inner "Vì mình cũng từng nhìn vào gương bằng ánh mắt y vậy."

    ## The reveal — it's a paper knife
    scene_desc "Mei nhìn kỹ hơn. Con dao... Lưỡi bằng giấy."
    scene_desc "Dao giấy. Rọc giấy xịn bằng giấy."

    mei_inner "... Dao giấy."
    mei_inner "Lưỡi dao bằng giấy."
    mei_inner "Nó... Không thể cắt được cái gì."

    ## CHOICE: How Mei processes this
    menu:
        mei_inner "..."

        "Nhẹ nhõm, rồi thương — nó tuyệt vọng tới mức dùng dao giấy":
            $ empathy += 8
            $ self_worth += 3
            mei_inner "Nhẹ nhõm... Vì nó không thể tự làm đau mình bằng cái đó."
            mei_inner "Nhưng..."
            mei_inner "Thương. Vì nó tuyệt vọng tới mức cầm dao giấy."
            mei_inner "Nó biết dao giấy không cắt được. Nhưng nó vẫn cầm."
            mei_inner "Vì nó cần... Cầm một cái gì đó. Để cảm thấy mình có quyền kiểm soát."
            mei_inner "..."
            mei_inner "Mình hiểu. Mình hiểu cảm giác đó."

        "Nực cười — tất cả chỉ là drama":
            $ facade += 3
            $ empathy -= 5
            mei_inner "Dao giấy. Seriously."
            mei_inner "Drama cho vui hả."
            mei_inner "... Nhưng mà..."
            mei_inner "Sao mình lại giận? Giận vì... Sao?"
            mei_inner "Giận vì nó gây hoảng? Hay giận vì..."
            mei_inner "Nó dám thể hiện nỗi đau. Còn mình thì... Giấu."

        "Ngồi xuống — không biết nói gì, nhưng không bỏ đi":
            $ empathy += 5
            $ facade -= 5
            scene_desc "Mei ngồi phịch xuống đất. Cách Pi vài bước."
            mei_inner "Mình không biết nói gì."
            mei_inner "Mình chưa bao giờ giỏi chuyện an ủi. Toàn nói script."
            mei_inner "Nhưng lúc này... Script nào cũng vô dụng."
            mei_inner "Nên mình chỉ... Ngồi đây."

    ## The conversation
    scene_desc "Yên lặng kéo dài. Rồi Pi ngồi xuống, đối diện Mei."

    pi "..."
    mei "..."
    pi "*hự* Cái dao... Nó bằng giấy."
    mei "... Biết."
    pi "Vậy sao mày có mặt ở đây?"
    mei "... Không biết."

    mei_inner "Thật. Mình không biết."
    mei_inner "Chân mình tự đưa mình tới đây."

    pi "..."
    pi "*nói bằng giọng rất lạ — cao, nhẹ, run run*"
    pi "Mày... có biết cảm giác... bị ghét vì một thứ mình không kiểm soát được không?"

    mei_inner "..."
    mei_inner "Có."
    mei_inner "Mình biết."
    mei_inner "Mình bị ghét vì không hoàn hảo. Và mình ghét bản thân vì điều đó mỗi ngày."

    ## CHOICE: How Mei responds
    menu:
        mei_inner "Nó đang hỏi thật. Mình..."

        "Nói thật — \"Biết. Mình cũng bị ghét mỗi ngày.\"":
            $ facade -= 10
            $ empathy += 10
            $ self_worth += 5
            $ pi_bond += 20
            $ helped_pi = True
            mei "Biết."
            pi "... Hả?"
            mei "Mình biết cảm giác đó."
            mei "Bị ghét vì thứ mình không kiểm soát. Bị đánh giá vì thứ bề ngoài."
            mei "Mày vì giọng nói. Mình vì... Rất nhiều thứ."
            pi "... Mày? Mai Trần? Bị ghét?"
            mei "*cười nhạt* Mày nghĩ top 1 khối thì không khổ hả?"
            mei "Top 1 khối nghĩa là ai cũng soi. Ai cũng chờ mày trượt. Ai cũng mong mày fail."
            mei "Và nếu mày fail... Bọn họ sẽ vui."
            pi "..."
            mei "Nhưng mà..."
            mei "Mày biết sao không? Có những thứ mình nghĩ là yếu điểm..."
            mei "Đôi khi lại là thứ mạnh nhất."
            pi "Giọng tao mạnh chỗ nào? Bị chọc mỗi ngày!"
            mei "Thì... Mình chưa nghe mày hát."
            mei "Nhưng giọng lạ... Đôi khi lại hay."

            scene_desc "Pi nhìn Mei, lần đầu có ánh sáng trong mắt."

        "Im lặng, nhưng ở lại — sự hiện diện là đủ":
            $ empathy += 5
            $ facade -= 3
            $ pi_bond += 10
            $ helped_pi = True
            mei "..."
            scene_desc "Mei không nói gì. Chỉ ngồi."
            scene_desc "Pi nhìn Mei. Mei nhìn Pi."
            scene_desc "Im lặng. Nhưng không khó chịu."
            mei_inner "Đôi khi... Người ta không cần lời nói."
            mei_inner "Chỉ cần biết ai đó... Ở đây."
            pi "... Tao không biết sao mày ở đây."
            pi "Nhưng... Cám ơn. Chắc vậy."
            mei_inner "..."
            mei_inner "Lần đầu tiên mình không cần nói gì... Mà ai đó vẫn biết ơn."

        "Nói một câu rồi đi — không giỏi mấy chuyện này":
            $ facade += 2
            $ empathy += 2
            $ pi_bond += 5
            mei "Đừng làm chuyện ngu."
            pi "... Hả?"
            mei "Dao giấy. Seriously? Nếu mày muốn thay đổi cái gì đó, thì đổi cách nghĩ. Không phải đổi thanh quản."
            scene_desc "Mei đứng dậy, phủi quần."
            mei "Bye."
            scene_desc "Mei đi đi mà không ngoái lại."
            mei_inner "... Lời nói đó đúng hay sai?"
            mei_inner "Mình không biết. Mình chưa bao giờ tự tin khi nói thật."
            mei_inner "Nhưng ít nhất... Mình đã nói."

    ## --------------------------------------------------------
    ## PART 4: VY VÀ PI — WITNESSING THE MAGIC
    ## --------------------------------------------------------

    scene_desc "Mei đi xa một chút, nhưng... Quay lại nhìn."

    mei_inner "... Mình không nên ở đây. Nhưng..."

    scene_desc "Từ hướng khác, Vy xuất hiện. Tay cầm máy ảnh."

    mei_inner "Vy?"
    mei_inner "Nó... Gặp Pi?"

    scene_desc "Mei nấp sau cây cột, quan sát."

    scene_desc "Vy nói chuyện với Pi. Cái kiểu nói... Bình thường. Thẳng thắn. Không script."

    vy "Ê! Mày có bao giờ thử hát chưa?"
    pi "Gì? Hát? Chưa bao giờ!"
    vy "Thử hát xem!"

    mei_inner "... Hát? Vy bảo nó hát?"
    mei_inner "Với cái giọng đó?"
    mei_inner "Vy điên rồi..."

    scene_desc "Vy bật điện thoại, chọn nhạc. Pi miễn cưỡng nhìn theo."
    scene_desc "Rồi Pi... Hát."

    ## [SFX/MUSIC: pi_singing — placeholder for Pi's singing scene]
    scene_desc "Giọng hát vang lên. Và..."
    scene_desc "Không giống nói. Hoàn toàn khác."
    scene_desc "Cao. Trong. Thanh. Như... Thiên thần."

    mei_inner "..."
    mei_inner "Gì... Vậy?"
    mei_inner "Giọng đó... Là giọng PI?"
    mei_inner "Giọng nói thì bị chọc, bị ghét, bị khinh."
    mei_inner "Nhưng giọng hát... Giọng hát..."

    scene_desc "Mei đứng sau cột, mắt mở to, miệng hé."

    mei_inner "Đẹp."
    mei_inner "Đẹp tới mức... Mình quên thở."

    scene_desc "Pi hát xong. Nhìn Vy. Vy giơ ngón cái, cười. Pi cười."

    vy "Sao nào ngài 'Giọng Thiên Thần'. Cảm thấy bất ngờ bởi tài năng của mình chưa?"
    pi "Tao... Sao trước giờ tao không nhận ra điều này..."

    mei_inner "..."
    mei_inner "Máy Ảnh Sự Thật."
    mei_inner "Nó chụp Pi... Và thấy 'Angel's Voice'."
    mei_inner "Nó thấy bản chất thật của Pi."
    mei_inner "Thứ mà Pi tưởng là lời nguyền... Lại là món quà."

    ## CHOICE: What does this mean for Mei?
    mei_inner "Nếu bản chất thật của Pi là 'Giọng Thiên Thần'..."
    menu:
        mei_inner "Thì bản chất thật của mình là gì?"

        "Có lẽ mình cũng có gì đó đẹp bị giấu đi":
            $ self_worth += 8
            $ empathy += 3
            mei_inner "Mình đã giấu bản thân quá lâu."
            mei_inner "Giấu sau điểm 10. Giấu sau nụ cười. Giấu sau 9 clone accounts."
            mei_inner "Nhưng nếu Pi — cái giọng mà ai cũng ghét — lại chứa thiên thần..."
            mei_inner "Thì biết đâu... Dưới mặt nạ mình..."
            mei_inner "Cũng có gì đó... Đáng để thấy."
            mei_inner "... Lần đầu tiên mình nghĩ vậy."

        "Mình thì khác. Mình không có 'bản chất tốt đẹp' nào":
            $ self_worth -= 5
            $ facade += 3
            mei_inner "Pi may mắn hơn mình."
            mei_inner "Nó có tài năng ẩn giấu. Mình thì..."
            mei_inner "Mình chỉ có mặt nạ. Gỡ ra thì... Trống."
            mei_inner "Đừng so sánh. Mình và Pi khác nhau."
            mei_inner "Pi có bản chất. Mình chỉ có vai diễn."

        "Vy... Vy giúp người ta tìm thấy chính mình":
            $ empathy += 5
            $ vy_relationship += 10
            mei_inner "Vy không phải đứa bình thường."
            mei_inner "Mình đã nhầm."
            mei_inner "Nó cầm máy ảnh — chụp — và chỉ cho Pi thấy chính Pi."
            mei_inner "Đơn giản thế thôi."
            mei_inner "Nhưng nó làm được điều mà mình không bao giờ dám:"
            mei_inner "Nhìn thẳng vào sự thật."

    ## --------------------------------------------------------
    ## PART 5: VY NÓI VỚI PI — LỜI TẠM BIỆT
    ## --------------------------------------------------------

    scene_desc "Vy vỗ vai Pi."
    vy "Tốt rồi, tốt rồi. Giờ thì mày có thể tự hào về giọng của mày."
    vy "Nhớ là, đừng để sự tự ti cản bước mày."
    pi "... OKAY!!!"

    scene_desc "Vy bước đi. Pi ở phía sau, vẫy tay."
    pi "*la lên bằng giọng cao* Thank youuu! Thank youuuuuu! Mày là cứu tinh của tao!"

    scene_desc "Vy quay lại chào, rồi đi tiếp."

    mei_inner "..."
    mei_inner "Vy đi rồi. Pi đứng đó, cười."
    mei_inner "Và mình... Vẫn đứng sau cái cột."
    mei_inner "Nấp. Quan sát. Như mọi khi."
    mei_inner "Luôn luôn ở ngoài. Luôn luôn nhìn vào."
    mei_inner "Không bao giờ tham gia."

    ## CHOICE: Step out or stay hidden?
    menu:
        mei_inner "..."

        "Bước ra — đi nói chuyện với Pi":
            $ facade -= 8
            $ empathy += 8
            $ pi_bond += 15
            $ helped_pi = True
            scene_desc "Mei bước ra khỏi cái cột. Pi giật mình."
            pi "!? Mai?"
            mei "... Giọng mày... Thật sự hay."
            pi "Mày... Nghe hết hả?"
            mei "... Ờ."
            pi "..."
            mei "... Mình biết cảm giác bị ghét vì thứ bề ngoài."
            mei "Nhưng mày vừa chứng minh rằng bề ngoài không phải là tất cả."
            mei "Nên... Cám ơn."
            pi "... Cám ơn??? Tao phải cám ơn mới đúng chứ..."
            mei "*lắc đầu, cười nhẹ — lần này thật* Mày cho mình thấy... Có thể bên dưới mặt nạ... Vẫn còn gì đó."
            pi "???"
            mei "Kệ. Bye."
            scene_desc "Mei đi nhanh, không ngoái lại. Nhưng Pi đứng nhìn theo, confused nhưng... Ấm."

        "Ở yên — chưa sẵn sàng":
            $ facade += 2
            mei_inner "Không. Mình không biết nói gì."
            mei_inner "Và mình không sẵn sàng để ai nhìn thấy mình... Thật."
            mei_inner "Chưa."
            scene_desc "Mei đứng sau cột cho đến khi Pi đi rồi. Rồi mới bước ra."
            mei_inner "Một mình. Như mọi khi."
            mei_inner "Nhưng hôm nay..."
            mei_inner "Hôm nay 'một mình' có vị khác."

    ## --------------------------------------------------------
    ## PART 6: ĐƯỜNG VỀ — REFLECTION
    ## --------------------------------------------------------

    ## [BG: bg street_evening — Evening walk]
    scene_desc "Mei đi bộ về nhà. Tai nghe không cắm. Lần đầu tiên."

    mei_inner "Hôm nay mình thấy..."
    mei_inner "Một thằng con trai tưởng mình vô giá trị."
    mei_inner "Vì cái giọng nói. Cái thứ mà nó sinh ra đã có."
    mei_inner "Và rồi... Cái giọng đó lại là thứ đẹp nhất về nó."

    pause 0.5

    mei_inner "Vậy những thứ mình ghét về bản thân..."
    mei_inner "Sự nhạy cảm. Sự cầu toàn. Sự cô đơn."
    mei_inner "Những clone accounts lúc 3 giờ sáng. Mì tôm nửa đêm. Deep web."
    mei_inner "Tất cả những thứ 'weird' đó..."
    mei_inner "Có phải cũng là... Một phần của điều gì đó?"

    pause 0.5

    mei_inner "Mình không biết."
    mei_inner "Nhưng hôm nay... Cái vết nứt trên pháo đài..."
    mei_inner "Nó hơi rộng hơn một tí."
    mei_inner "Và qua vết nứt đó..."
    mei_inner "Sáng hơn."

    jump chapter4_end
